from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = "Secret key for weekend demo"

@app.route('/')
def index():
    if not 'moments' in session:
        session['moments'] = []
    print session["moments"]    
    return render_template('index.html', moments=session['moments'])

@app.route('/moments/create', methods=["POST"])   
def create():
    moment = {
        "id":random.randint(0,100000000),
        "text":request.form['text'],
        "title":request.form['title']
    } 
    temp = session['moments']
    temp.append(moment)
    session['moments'] = temp
    # session.clear()
    return redirect('/')

@app.route('/show/<m_id>')  
def show(m_id):
    show_moment = {}
    for moment in session["moments"]:
        if int(moment['id']) == int(m_id):
            show_moment = moment
    return render_template("show.html", moment=show_moment)  

app.run(debug=True)    