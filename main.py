import sqlite3
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

OPEN_WEATHER = "285d185794f6e2171dfbd9b519bfdd5e"
IP_STACK = '4e1e637f44cbe81663c408e961bd611b'

@app.route('/')
@app.route('/index.html')
def index():
    conn = sqlite3.connect("site_data.db")
    cursor = conn.execute("SELECT User, Content, Likes, rowid from messages ORDER BY Likes DESC ")
    records = cursor.fetchall()
    cursor = conn.execute("SELECT DISTINCT location FROM messages");
    locations = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("index.jinja2", messages=records, msg_locations=locations)


@app.route('/about.html')
def about():
    return render_template("about.jinja2")

@app.route('/stuff.html')
def stuff():
    return render_template("stuff.jinja2")

@app.route('/message.html', methods=['POST'])
def custom():
    author = request.form['author']
    loc_data = get_location_data(request.remote_addr)
    author = author + 'from %s,%s' % (loc_data['city'], loc_data['region_code'])
    message = request.form['message']

    conn = sqlite3.connect("site_data.db")
    # Add new
    location = '%s/%s' % (loc_data['country_code'], loc_data['region_code'])
    location = location.lower()
    cursor = conn.execute("INSERT INTO messages VALUES (?,?, 0, ?)", (author, message, location))
    cursor.close()
    conn.commit()
    conn.close()
    print("[%s] posted '%s'" % (author, message))

    return render_template('thanks.jinja2')

@app.route('/weather.html')
def weather():
    loc_data = get_location_data(request.remote_addr)
    lat = loc_data['latitude']
    lon = loc_data['longitude']
    (temperature, weather_descr) = get_weather_data(lat, lon)
    if temperature > 69:
        temperature_style = "text-danger"
    else:
        temperature_style = 'text-primary'
    return render_template('weather.jinja2',
        weather_desc = weather_descr,
        temperature_style = temperature_style,
        temperature = "%0.2f" % temperature)

@app.route('/like.html')

def like():
    rowid = request.args['rowid']
    conn = sqlite3.connect("site_data.db")
    cursor = conn.execute("SELECT Likes from messages WHERE rowid=?", (rowid, ))
    record = cursor.fetchone()
    likes = record[0]
    print(record)
    cursor.close()
    cursor = conn.execute("UPDATE messages SET Likes=? WHERE rowid=?", (likes+1, rowid))
    conn.commit()
    cursor.close()
    conn.close()
    return render_template('thanks.jinja2')
    #minor change


def get_weather_data(lat, lon):
    resp = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=285d185794f6e2171dfbd9b519bfdd5e' % (
       lat, lon))
    result = resp.json()
    desc = result['weather'][0]['description']
    temp = (result['main']['temp'] - 273.15)*(9/5)+32
    return temp, desc

def get_location_data(ip_addr):
    resp = requests.get("http://api.ipstack.com/%s?access_key=%s"%(ip_addr,IP_STACK))
    result = resp.json()
    if result['latitude'] is None:
        result['city'] = 'Annapolis'
        result['latitude'] = 38.98
        result['longitude'] = -76.48
        result['country_code'] = 'US'
        result['region_code'] = 'MD'
        result['region_name'] = "Maryland"
    return result