from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisisSecret'

@app.route('/')
def index():
    session['index_counter'] = 0
    print "*******"*10
    print(session['index_counter'])
    print "*******"*10
    return redirect('/next')

@app.route('/next')  
def next():  
    session['index_counter'] += 1
    return render_template("index.html", index_counter=session['index_counter'])

@app.route('/ninja')
def ninja():
    session['index_counter'] += 2
    return render_template("index.html", index_counter=session['index_counter'])    

@app.route('/hack')
def hack():
    session['index_counter'] = 1
    return render_template("index.html", index_counter=session['index_counter']) 

app.run(debug=True)    