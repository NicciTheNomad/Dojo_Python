from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "KeepItSimpleStupid"

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

mysql = MySQLConnector(app,'full_friends')

@app.route('/')
def index():
    query = 'SELECT * FROM friends'
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)
# -----------------
@app.route('/friends/create', methods=["POST"])   
def create():
    query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
    data = {
        'first_name': request.form['first_name'], 
        'last_name':  request.form['last_name'],
        'email': request.form['email']
    }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/edit/<friend_id>')
def edit(friend_id):
     
    query = "SELECT * FROM friends WHERE id = :id_of_friend"
    data = {"id_of_friend":friend_id}
    try:
        friend = mysql.query_db(query, data)[0]
    except IndexError:
        return redirect('/')

    return render_template('edit.html', friend=friend)  

@app.route('/display_update/<friend_id>', methods=['POST'])
def update(friend_id):
    query = "UPDATE friends SET first_name = :set_first_name, last_name = :set_last_name, email = :set_email WHERE id = :id"
    data = {
                'set_first_name': request.form['update_first_name'],
                'set_last_name': request.form['update_last_name'],
                'set_email': request.form['update_email'],
                'id': friend_id
            }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/delete/<friend_id>', methods=["POST"])
def delete(friend_id):
    query = "DELETE FROM friends WHERE id = :id" 
    data = {
        'id': friend_id
        }
    mysql.query_db(query, data)   
    return redirect('/')

app.run(debug=True)




# i thought it need to accept post and then i tried methods=['GET, POST']

# ta_wes
# 11:03 PM
# no, you definitely DO NOT want to do that

# 11:03 PM
# That would allow anyone to put anything they want into the url bar in their browser and directly modify your database

# 11:03 PM
# that's bad
# ------------
#@app.route('/delete/<friend_id>', methods=["GET", "POST"])
# def delete(friend_id):
#     query = "DELETE FROM friends WHERE id = :id" 
#     data = {
#         'id': friend_id
#         }
#     mysql.query_db(query, data)   
#     return redirect('/')