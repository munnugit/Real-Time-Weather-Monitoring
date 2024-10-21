from flask import Flask, render_template, request, jsonify, redirect
import requests
from datetime import datetime

app = Flask(__name__)

# Replace with your actual WeatherAPI key
API_KEY = 'your_weatherapi_key'
CITIES = ['City1', 'City2', 'City3']  # Add your desired cities

weather_data = {}
daily_summary = {}
alerts = []

def fetch_weather():
    global weather_data, daily_summary, alerts
    weather_data = {}
    for city in CITIES:
        response = requests.get(f'https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}')
        data = response.json()
        
        city_name = data['location']['name']
        condition = data['current']['condition']['text']
        temp = data['current']['temp_c']
        feels_like = data['current']['feelslike_c']
        last_updated = datetime.strptime(data['current']['last_updated'], '%Y-%m-%d %H:%M')

        weather_data[city_name] = {
            'condition': condition,
            'temp': temp,
            'feels_like': feels_like,
            'dt': last_updated
        }

        date = last_updated.strftime('%Y-%m-%d')
        if date not in daily_summary:
            daily_summary[date] = {'total_temp': 0, 'count': 0, 'max_temp': float('-inf'), 'min_temp': float('inf'), 'dominant_condition': condition}
        daily_summary[date]['total_temp'] += temp
        daily_summary[date]['count'] += 1
        daily_summary[date]['max_temp'] = max(daily_summary[date]['max_temp'], temp)
        daily_summary[date]['min_temp'] = min(daily_summary[date]['min_temp'], temp)
        daily_summary[date]['dominant_condition'] = condition

    check_alerts()

def check_alerts():
    global alerts
    alerts = []  # Reset alerts
    for city, data in weather_data.items():
        for alert in alerts:
            if data['temp'] > alert['temperature'] and data['condition'].lower() == alert['condition'].lower():
                alerts.append(f'Alert! {city} is experiencing {data["condition"]} with a temperature of {data["temp"]}°C!')

@app.route('/')
def index():
    fetch_weather()  # Fetch weather data on index load
    return render_template('index.html', weather_data=weather_data, daily_summary=daily_summary, alerts=alerts)

@app.route('/update_weather', methods=['GET'])
def update_weather():
    fetch_weather()  # Fetch the latest weather data
    return jsonify({'weather_data': weather_data, 'daily_summary': daily_summary, 'alerts': alerts})

@app.route('/set_alert', methods=['POST'])
def set_alert():
    temperature = request.form['temperature']
    condition = request.form['condition']
    alerts.append({'temperature': float(temperature), 'condition': condition})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
