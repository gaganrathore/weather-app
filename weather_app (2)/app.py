from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

recent_searches = []

@app.route('/')
def index():
    return render_template('index.html', recent_searches=recent_searches)

@app.route('/geocode', methods=['POST'])
def geocode():
    data = request.json
    city = data.get('city')
    if not city:
        return jsonify({'error': 'City name is required'}), 400

    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
    response = requests.get(geo_url)
    geo_data = response.json()

    if 'results' not in geo_data:
        return jsonify({'error': 'City not found'}), 404

    location = geo_data['results'][0]
    lat, lon = location['latitude'], location['longitude']
    name, country = location['name'], location.get('country', '')

    return jsonify({'lat': lat, 'lon': lon, 'city': name, 'country': country})

@app.route('/weather', methods=['POST'])
def weather():
    data = request.json
    lat, lon = data.get('lat'), data.get('lon')
    city = data.get('city')

    if not lat or not lon:
        return jsonify({'error': 'Latitude and Longitude are required'}), 400

    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min,"
        f"precipitation_probability_max,weathercode&timezone=auto&current_weather=true"
    )
    response = requests.get(weather_url)
    weather_data = response.json()

    if city not in recent_searches:
        recent_searches.insert(0, city)
        if len(recent_searches) > 5:
            recent_searches.pop()

    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)