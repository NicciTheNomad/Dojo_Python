from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = "thisisasecretkey"

@app.route('/')
def index():
    print 'in index route'
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    print 'in process route' *3
    if len(request.form['name']) == 0:
        flash('Name can not be empty')
    if len(request.form['description']) < 1:  
        flash('Description can not be empty.') 
    if len(request.form['description']) > 121:
        flash('Description must be 120 characters or less.')  
    if len(request.form['language']) < 2:
        flash('select a language') 
    if len(request.form['location']) < 2:
        flash('select a location')          
    else:
        print 'in the else statement'*3
        flash("Thank you {}".format(request.form['name']))
        # return redirect('/')   
    session['submitted_info'] = request.form
    print "after submitted-info**********"*2
    return redirect('/submitted')


@app.route('/submitted')  
def submit():
    return render_template('submitted.html', result=session['submitted_info']) 

app.run(debug=True)    