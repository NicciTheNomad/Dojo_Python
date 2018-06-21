from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)
app.secret_key = "keepitsafestupid"

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def submit():
  first_name = request.form['first_name']
  last_name = request.form['last_name']
  email = request.form['email']
  password = request.form['password']
  confirm_password = request.form['confirm_password']
  print '8' * 50
  print first_name 
  print last_name
  print email
  print password
  print confirm_password
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
  if password == "" or len(password) < 4:
    flash('password must be 4 characters and match confirm password') 
    valid = False
  if confirm_password != password:
    flash('password must be 4 characters and match confirm password')  
    valid = False 

  if valid == True:
    return "User is Registered!"  
  elif valid == False:
    return redirect('/')   


app.run(debug=True)       