import requests
import configparser
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def weather_dashboard():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def render_results():
    zip_code = request.form['zipCode']
    #return 'Zip Code: '+zip_code
    api_key = get_api_key()
    data = get_weather_results(zip_code, api_key)
    temp = "{0:.2f}".format(data["main"]["temp"])
    feels_like = "{0:.2f}".format(data["main"]["feels_like"])
    weather = data["weather"][0]["main"]
    location = data["name"]

    return render_template('results.html'
                           , location=location, temp=temp,feels_like=feels_like,weather=weather)

def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']

def get_weather_results(zip_code,api_key):
    api_key = 'http://api.openweathermap.org/data/2.5/weather?zip={}&units=metric&appid={}'.format(zip_code,api_key)
    req = requests.get(api_key)
    return req.json()

if __name__ =='__main__':
    app.run(debug=True)


#get_weather_results(20540,get_api_key())