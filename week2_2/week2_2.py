from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "Secret Stuff"

@app.route('/')
def index():
    if "name" in session:
        return redirect('/hello/' + session["name"])
    name = "Minh"
    students = [
        {'first_name':'Kyle', 'last_name':'Abueg'},
        {'first_name':'Chris', 'last_name':'Abueg'},
        {'first_name':'Nickolas', 'last_name':'Abueg'},
        {'first_name':'Will', 'last_name':'Abueg'},
        {'first_name':'Oliver', 'last_name':'Abueg'},            
    ]
    return render_template('index.html', x=name, all_students=students)

@app.route('/i/moments/<moment_id>')   
def moment(moment_id):
    return moment_id

@app.route('/hello/<name>')   
def hello(name):
    return render_template("hello.html", name=name)

@app.route('/process', methods=["POST"])   
def process():
    if request.form["action"] == "register":  
        pass
    elif request.form["action"] == "login":
        session["name"] = request.form["first_name"]
        return redirect('/hello/' + session["name"]) 

@app.route('/logout', methods=["GET"])        
def logout():
    session.clear()
    return redirect('/')
app.run(debug=True)    