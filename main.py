import sqlite3
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    conn = sqlite3.connect("site_data.db")
    cursor = conn.execute("SELECT User, Content, Likes, rowid from messages ORDER BY Likes DESC ")
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("index.jinja2", messages=records)

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
    conn = sqlite3.connect("site_data.db")
    # Add new
    cursor = conn.execute("INSERT INTO messages VALUES (?, ?,0)" % (author, message))
    cursor.close()
    conn.commit()
    print("[%s] posted '%s'" % (author,message))

    return render_template('thanks.jinja2')

@app.route('/like.html')
def like():
    rowid = request.args['rowid']
    conn = sqlite3.connect("site_data.db")
    cursor = conn.execute("SELECT Likes from messages WHERE rowid=?", rowid)
    record = cursor.fetchone()
    likes = record[0]
    print(record)
    cursor.close()
    cursor = conn.execute("UPDATE messages SET Likes=? WHERE rowid=?", (likes+1, rowid))
    conn.commit()
    cursor.close()
    conn.close()
    #yo dawg
    return render_template('thanks.jinja2')