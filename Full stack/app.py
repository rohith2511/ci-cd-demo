from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# ✅ Add your API key here
API_KEY = '9928670c56f07978717c6e199ff7301a'

@app.route('/', methods=['GET', 'POST'])
def home():
    weather = None
    if request.method == 'POST':
        city = request.form['city']
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                'city': data['name'],
                'country': data['sys']['country'],
                'temp': data['main']['temp'],
                'description': data['weather'][0]['description'].title(),
                'icon': data['weather'][0]['icon']
            }
        else:
            weather = {'error': 'City not found!'}
    return render_template('index.html', weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
