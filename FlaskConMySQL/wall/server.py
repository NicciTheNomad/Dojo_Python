from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)

app.secret_key = "KeepItSimpleStupid"

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

mysql = MySQLConnector(app,'the_wall')
@app.route('/')
def index():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    return render_template('index.html', all_users = users)

@app.route('/register', methods=['POST'])
def reg():    
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    password = request.form["password"]
    confirm_password = request.form["confirm_password"]
    valid = True
    errors = []

    if first_name == '' or len(first_name) < 2:
        flash('first name cannot be blank, must have two characters')
        valid = False
    if last_name == '' or len(last_name) < 2:
        flash('last name cannot be blank, must have two characters') 
        valid = False
    if len(request.form['email']) < 1 or not EMAIL_REGEX.match(request.form['email']):
        flash("email can not be blank and must be valid")
        valid = False
    if password == "" or len(password) < 8:
        flash('password must be 8 characters and match confirm password') 
        valid = False
    if confirm_password != password:
        flash('password must be 8 characters and match confirm password')  
        valid = False 
    if valid == True:
        pw_hash = bcrypt.generate_password_hash(password) #is hash just a dictionary?-no
        insert_query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"   
        query_data = { 'first_name': first_name, 'last_name': last_name, 'email': email, 'pw_hash': pw_hash } 
        mysql.query_db(insert_query, query_data)

        query_newuser = 'SELECT * FROM users WHERE first_name=:new'
        data_newuser= {
            'new':first_name
        }
        user_newuser = mysql.query_db(query_newuser, data_newuser)
        try:    
            user_newuser = user_newuser[0]  
        except IndexError:
            return redirect('/') 

        session['id'] = user_newuser['id']
        flash("User is Registered!")
        return redirect('/logged_in')
    elif valid == False:
        return redirect('/')

@app.route('/login', methods=["POST"])
def login():
    first_name = request.form['first_name']
    password = request.form['password']
    query = 'SELECT * FROM users WHERE first_name=:one'    
    data = { 'one':first_name }
    user = mysql.query_db(query, data)
    print "above try statement for login ***"*3
    try:    
        user = user[0] 
    except IndexError:
        return redirect('/') 

    if bcrypt.check_password_hash(user['pw_hash'], password): 
        session['id'] = user['id']
        return redirect('/logged_in')
    else:
        flash('invalid password and / or first name')
        return redirect('/')
    return 'end of /login route'

@app.route('/store_message', methods = ["POST"])
def store_message():
    message = request.form["message"]
    query = "INSERT INTO messages (message, created_at, updated_at, users_id) VALUES (:message, NOW(), NOW(),:users_id)"
    data = {'message': message, "users_id": session['id']} 
    mysql.query_db(query, data)
    return redirect("/logged_in")


@app.route('/logged_in')
def logged_in():
    query = 'SELECT first_name FROM users WHERE id=:inject_one'
    data = {
        'inject_one':session['id']
    }
    logged_user = mysql.query_db(query, data)[0]
    # query_message = "SELECT * FROM messages"
    mysql.query_db(query, data)
    query_m = 'SELECT * FROM messages'
    messages = mysql.query_db(query_m)
    print logged_user
    print "&"*25
    return render_template('view.html', logged_user = logged_user, all_messages = messages)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')    

app.run(debug=True)     