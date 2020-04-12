from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/index.html')
def index():
    return render_template("index.jinja2")

@app.route('/about.html')
def about():
    return render_template("about.jinja2")

@app.route('/stuff.html')
def stuff():
    return render_template("stuff.jinja2")

@app.route('/custom.html', methods=['POST'])
def custom():
    user_first = request.form['fname']
    user_last = request.form['lname']
    return 'hi %s %s' %(user_first,user_last)