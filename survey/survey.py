# from flask import Flask, render_template, request
# app = Flask(__name__)

# @app.route('/')
# def survey():
#     return render_template('index.html')

# @app.route('/result', methods=['POST', 'GET'])
# def result():
#     if request.method == 'POST':
#         request = request.form
#         return render_template("form.html",result = result)

# if __name__ == '__main__':        
#     app.run(debug = True)


    # -----
#     name = request.form['name']
#     location = request.form['location']
#     language = request.form['language']
#     comment = request.form['comment']

# app.run(debug=True)
# --------------
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("form.html",result = result)

@app.route('/logout')        
def logout():
    return redirect('/')      

if __name__ == '__main__':
   app.run(debug = True)
