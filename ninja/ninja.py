from flask import Flask, render_template, redirect, session, flash, request, url_for

app = Flask(__name__)
app.secret_key = "shhh...it's secret"

@app.route('/')
def index():    
    return render_template('index.html')

@app.route('/ninjas/<ninja_color>')    
def ninjas(ninja_color):
    if ninja_color == "orange":
        character = "michelangelo" 
    elif ninja_color == 'blue':
        character = 'leonardo'
    elif ninja_color == 'red':
        character = 'raphael'
    elif ninja_color == 'purple':
        character = 'donatello'
    else:
        character = "notapril"
    return render_template('ninja.html', character=character)

app.run(debug=True)    
