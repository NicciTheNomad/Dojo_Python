from flask import Flask, render_template, request, redirect, session
import random
from random import randrange, randint
app = Flask(__name__)
app.secret_key = "ThisisSecret"

low = "Your Guess is Low"
high = "Your Guess is High"

def random():
    import random
    session['num'] = int(random.randrange(0, 101))
    return None

@app.route('/')
def index():
    print '*'*15
    random()
    print session['num']
    return render_template('index.html', num=session['num'])

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    print "*"*50
    print session['guess']
    print session['num']
    if session['guess'] == session['num']:
        return redirect('/correct')
    elif session['guess'] < session ['num']:
        print "in the GUESS else statement due to WRONG low answer" 
        print session['guess']
        return render_template('wrong.html', message=low)  
    else:
        return render_template('wrong.html', message=high)    

@app.route('/correct')
def correct():
    return render_template('correct.html', num=session['num'])        

app.run(debug=True)    