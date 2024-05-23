import os
import zipfile

# Create the folder structure and files for the weather dashboard application
base_dir = '/mnt/data/weather_dashboard'
os.makedirs(base_dir, exist_ok=True)

# Define file contents
app_py = """\
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_babel import Babel, gettext
from flask_compress import Compress
from flask_caching import Cache
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['CACHE_TYPE'] = 'simple'
db = SQLAlchemy(app)
cache = Cache(app)
Compress(app)
login_manager = LoginManager(app)
babel = Babel(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    theme = db.Column(db.String(10), default='light')
    units = db.Column(db.String(10), default='metric')
    locations = db.Column(db.Text, default='[]')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@login_required
def index():
    return render_template('index.html', user=current_user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/update_theme', methods=['POST'])
@login_required
def update_theme():
    current_user.theme = request.form['theme']
    db.session.commit()
    return jsonify({'success': True})

@app.route('/update_units', methods=['POST'])
@login_required
def update_units():
    current_user.units = request.form['units']
    db.session.commit()
    return jsonify({'success': True})

@app.route('/update_locations', methods=['POST'])
@login_required
def update_locations():
    current_user.locations = request.form['locations']
    db.session.commit()
    return jsonify({'success': True})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
"""

index_html = """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather Dashboard</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <div class="container">
        <h1 class="text-center">{{ _('Weather Dashboard') }}</h1>
        <div class="row">
            <div class="col-md-6">
                <input type="text" id="location-input" class="form-control" placeholder="{{ _('Enter location') }}" aria-label="{{ _('Enter location') }}">
            </div>
            <div class="col-md-6">
                <select id="unit-select" class="form-control" aria-label="{{ _('Select units') }}">
                    <option value="metric">{{ _('Metric') }}</option>
                    <option value="imperial">{{ _('Imperial') }}</option>
                </select>
            </div>
        </div>
        <button id="refresh-button" class="btn btn-primary mt-3" aria-label="{{ _('Refresh weather data') }}">{{ _('Refresh') }}</button>
        <button id="theme-toggle" class="btn btn-secondary mt-3" aria-label="{{ _('Toggle theme') }}">{{ _('Toggle Theme') }}</button>
        <div id="weather-data" class="mt-3"></div>
        <div id="forecast-data" class="mt-3"></div>
        <div id="alerts-data" class="mt-3"></div>
        <canvas id="myChart" width="400" height="200" class="mt-3"></canvas>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="{{ url_for('static', filename='js/script.js') }}"></script>
</body>
</html>
"""

script_js = """\
document.getElementById('refresh-button').addEventListener('click', function() {
    const location = document.getElementById('location-input').value || 'London';
    const units = document.getElementById('unit-select').value;
    fetch(`/weather/${location}?units=${units}`)
        .then(response => response.json())
        .then(data => {
            const tempUnit = units === 'metric' ? '°C' : '°F';
            const speedUnit = units === 'metric' ? 'm/s' : 'mph';
            document.getElementById('weather-data').innerHTML = `
                <p>Temperature: ${data.main.temp} ${tempUnit}</p>
                <p>Humidity: ${data.main.humidity} %</p>
                <p>Pressure: ${data.main.pressure} hPa</p>
                <p>Wind Speed: ${data.wind.speed} ${speedUnit}</p>
            `;
            updateCharts(data);
        });
});

document.getElementById('theme-toggle').addEventListener('click', function() {
    document.body.classList.toggle('dark-mode');
});

function updateCharts(data) {
    const ctx = document.getElementById('myChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Temperature', 'Humidity', 'Pressure', 'Wind Speed'],
            datasets: [{
                label: 'Current Weather',
                data: [data.main.temp, data.main.humidity, data.main.pressure, data.wind.speed],
                backgroundColor: 'rgba(0, 123, 255, 0.2)',
                borderColor: 'rgba(0, 123, 255, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}
"""

style_css = """\
body {
    background-color: white;
    color: black;
}

body.dark-mode {
    background-color: #121212;
    color: #e0e0e0;
}

.dark-mode .btn-primary {
    background-color: #444;
    border-color: #555;
}

.dark-mode .form-control {
    background-color: #333;
    color: #e0e0e0;
    border-color: #555;
}

.dark-mode canvas {
    background-color: #222;
}

.container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}

button {
    margin-top: 10px;
}
"""

env_file = """\
SECRET_KEY=your_local_secret_key
API_KEY=your_openweathermap_api_key
DATABASE_URL=sqlite:///your_local_db.sqlite
"""

requirements_txt = """\
Flask==2.0.2
Flask-SQLAlchemy==2.5.1
Flask-Login==0.5.0
Flask-Babel==2.0.0
Flask-Compress==1.10.1
Flask-Caching==1.10.1
python-dotenv==0.19.2
gunicorn==20.1.0
requests==2.26.0
"""

# Create necessary directories
os.makedirs(os.path.join(base_dir, 'templates'), exist_ok=True)
os.makedirs(os.path.join(base_dir, 'static/css'), exist_ok=True)
os.makedirs(os.path.join(base_dir, 'static/js'), exist_ok=True)

# Write files to the appropriate locations
with open(os.path.join(base_dir, 'app.py'), 'w') as f:
    f.write(app_py)

with open(os.path.join(base_dir, 'templates/index.html'), 'w') as f:
    f.write(index_html)

with open(os.path.join(base_dir, 'static/js/script.js'), 'w') as f:
    f.write(script_js)

with open(os.path.join(base_dir, 'static/css/style.css'), 'w') as f:
    f.write(style_css)

with open(os.path.join(base_dir, '.env'), 'w') as f:
    f.write(env_file)

with open(os.path.join(base_dir, 'requirements.txt'), 'w') as f:
    f.write(requirements_txt)

# Create a zip file of the directory
zip_filename = '/mnt/data/weather_dashboard.zip'
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), base_dir))

zip_filename