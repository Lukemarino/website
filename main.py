from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template("index.jinja2")

@app.route('/about.html')
def about():
    return render_template("about.jinja2")

@app.route('/stuff.html')
def stuff():
    return render_template("stuff.jinja2")

@app.route('/message.html', methods=['POST'])
def custom():
    author = request.form['author']
    message = request.form['message']
    print("[%s] posted '%s'" % (author,message))

    return render_template('new_message.jinja2')