from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/users', methods=['POST'])

def create_user():
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms

   name = request.form['name']
   print name
   email = request.form['email']
   print email
   user = request.form
   return render_template('display_users.html', user = user)
#    return redirect('display_users/<name>', user = user)

@app.route('/display_users/<name>')
def display_users(name):
    # print email
    return render_template('display_users.html') 
app.run(debug=True) # run our server
