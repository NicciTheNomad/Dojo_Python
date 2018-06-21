from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
@app.route('/')
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)
@app.route('/friends', methods=["POST"])
def create():
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUE (:first_name, :last_name, :occupation, NOW(), NOW())"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'occupation': request.form['occupation']
    }
    mysql.query_db(query, data)
    return redirect('/')    
@app.route('/update_friend/<friend_id>')
def update(friend_id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
    data = {
             'first_name': 'emma', 
             'last_name':  'sanyal',
             'occupation': 'mi amiga',
             'id': friend_id
           }
    mysql.query_db(query, data)
    return redirect('/')

def create():
    # add a friend to the database!
    return redirect('/')
app.run(debug=True)
