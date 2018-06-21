from flask import Flask, render_template, request, redirect, session
import random
from random import randrange, randint
app = Flask(__name__)
app.secret_key = "ThisisSecret"

def ninja_gold():
    import random
    session['ninja_gold'] = int(0)
    print session['ninja_gold']
    return None

def farm_money():
    import random
    session['farm']=int(random.randrange(9-21))
    return None

def cave_money():
    import random
    session['cave']=int(random.randrange(4-11))
    return None

def house_money():
    import random
    session['house']=int(random.randrange(1-6))
    return None

def casino_money():
    import random
    session['casino']=int(random.randrange(-50-51)) 
    return None   

@app.route('/')
def index():
    print '*'*15
    ninja_gold()
    if session['guess'] = request.form['guess']
    print session['ninja_gold']
    return render_template('ninja.html', num=session['ninja_gold'])
    
# @app.route('/ninja_gold')    
# def ninja_gold():
#     ninja_gold()
#     if session['guess']:
        # farm_money()
        # ninja_gold += farm_money
    #     ninja_gold +=10
    #     print "@"*15
    #     print ninja_gold
    # return render_template('ninja.html', num=session['ninja_gold'])

app.run(debug=True)    

    

