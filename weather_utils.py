import requests

API_KEY = "b34f09a8bbadb6543a1fd42113cbc754"  # Replace with your OpenWeatherMap API key

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + API_KEY + "&q=" + city + "&units=metric"
    response = requests.get(complete_url)
    return response.json()

def process_weather_data(data):
    # Extract necessary information from the API response
    today_weather = {
        'temp': data['main']['temp'],
        'min': data['main']['temp_min'],
        'max': data['main']['temp_max'],
        'desc': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon']
    }
    return {'today': today_weather}
