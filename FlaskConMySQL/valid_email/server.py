from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "KeepItSimpleStupid"

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

mysql = MySQLConnector(app,'valid_email')
@app.route('/')
def index():
    print "*"*10,'in index'   
    query = "SELECT * FROM users"
    users = mysql.query_db(query) 
    return render_template('index.html', all_users=users)

@app.route('/email_check', methods=['POST'])
def email_check():
    email = request.form['email']
    valid = True
    
    if email == '' or len(email) < 5:
        valid = False
    if len(request.form['email']) < 1 or not EMAIL_REGEX.match(request.form['email']):
        valid = False     
    if valid == True:
        query = "INSERT INTO users (email, created_at, updated_at) VALUE (:email, NOW(), NOW())"
        data = {
            'email': request.form['email']
        }
        mysql.query_db(query, data)
        flash("Thank you for the valid email: " + request.form['email'] + "!")    
        return redirect('/valid')
    elif valid == False:
        flash("email can not be blank and must be valid")
        return redirect('/')          

@app.route('/valid')
def valid_user():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    return render_template('valid.html', all_users=users)

@app.route('/delete')
def delete_record():
    query = "DELETE FROM users WHERE id = :id"
    data = {
                'id': request.form['delete_user']
            }    
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)    