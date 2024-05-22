from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

@app.route('/', methods=['GET'])
def weather_dashboard():
    city = request.args.get('city', 'London')

    # Fetch detailed forecast data
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(forecast_url)
    forecast_data = response.json()

    return render_template('dashboard.html', forecast=forecast_data, city=city)

if __name__ == '__main__':
    app.run(debug=True)