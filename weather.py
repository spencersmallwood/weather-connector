from flask import Flask, render_template
import requests

app = Flask(__name__)

# Replace with your actual OpenWeather API key
API_KEY = '1ac0268fd657e1b1f1bcbae45d60f396'

# Replace with the desired GPS coordinates
latitude = '30.408489421849378'
longitude = '-97.65117496608931'

@app.route('/')
def index():
    weather_data = fetch_weather_data()
    return render_template('index.html', weather_data=weather_data)

def fetch_weather_data():
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=imperial&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == '__main__':
    app.run(debug=True)
