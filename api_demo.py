import requests

OPEN_WEATHER = "285d185794f6e2171dfbd9b519bfdd5e"
IP_STACK = '4e1e637f44cbe81663c408e961bd611b'
def main():
        resp = requests.get("http://api.ipstack.com/check?access_key=%s" % IP_STACK)
        result = resp.json()

        resp = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=285d185794f6e2171dfbd9b519bfdd5e' % (result['latitude'], result['longitude']) )
        result = resp.json()
        desc = result['weather'][0]['description']
        print("%s" % desc)


if __name__ == "__main__":
        main()
