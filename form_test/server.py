from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisisSecret'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/show')
def show_user():
    return render_template('test_form.html') 

@app.route('/users', methods=['POST'])
def create_user():
    print "Got post info"
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect('/show')

@app.route('/process', methods=['POST'])
def process():
    if request.form["action"] == "register":
        pass #do some registration
    elif request.form["action"] == "login":
        session['email'] = request.form['email']
        session['password'] = request.form['password']
        return redirect('/show')        

app.run(debug=True)    