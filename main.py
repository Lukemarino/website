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
    first = request.form['fname']
    last = request.form['lname']
    impress =  request.form['formControlRange']
    if thing < 50 :
        image.path= 'static/sad.jpg'
    else:
        image.path = 'static/stonks.jpg'
    name = first + "" + last
    return render_template('custom.jinja2', full_name = name, thing = impress )