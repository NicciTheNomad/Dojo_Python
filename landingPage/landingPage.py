from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", phrase="nicci")

@app.route('/ninjas')
def ninjas():
    return render_template('index.html', phrase='ray and nicci')

@app.route('/dojos/new')
def dojos():
    return render_template('index.html', phrase='ray and nicci and the kids')
    
app.run(debug=True)    