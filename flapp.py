from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# API keys from environment variables
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

# Flask app setup
app = Flask(__name__)

@app.route('/', methods=['GET'])
def dashboard():
    city = request.args.get('city', 'London')
    country = request.args.get('country', 'us')

    # Fetch detailed weather data including forecast
    weather_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={WEATHER_API_KEY}&units=metric"
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    # Fetch news data (remains unchanged)
    news_url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}"
    news_response = requests.get(news_url)
    news_data = news_response.json()
    
    if news_response.status_code != 200 or 'articles' not in news_data:
        news_data = {'articles': [{'title': 'News data not available for this country.', 'url': '#'}]}

    return render_template('dashboard.html', weather=weather_data, news=news_data['articles'])


if __name__ == '__main__':
    app.run(debug=True)