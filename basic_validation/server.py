from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "keepitsafestupid"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
# def process():
  # if len(request.form['name']) < 1:
    # flash("Name cannot be empty!") # just pass a string to the flash function
  # else: 
    # flash("Success! Your name is {}".format(request.form['name'])) # just pass a string to the flash function
  # return redirect('/') 
def submit():
  if len(request.form['email']) < 1:
    flash("email can not be blank")
  elif not EMAIL_REGEX.match(request.form['email']):
    flash('invalid email')  
  else:
    flash('thank you') 
  return redirect('/')   

app.run(debug=True)    