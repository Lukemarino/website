from flask import Flask, render_template
app = Flask(__name__)

@app.route('/index.jinja2')
def index():
    return render_template("index.jinja2")

@app.route('/about.jinja2')
def about():
    return render_template("about.jinja2")

@app.route('/stuff.jinja2')
def stuff():
    return render_template("stuff.jinja2")
