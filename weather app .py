import requests

# Replace with your OpenWeatherMap API key
API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetches weather data for the given city."""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Change to "imperial" for Fahrenheit
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        weather_info = {
            "City": data["name"],
            "Temperature": f"{data['main']['temp']}°C",
            "Humidity": f"{data['main']['humidity']}%",
            "Wind Speed": f"{data['wind']['speed']} m/s",
            "Weather": data["weather"][0]["description"].capitalize()
        }
        
        return weather_info
    else:
        return {"Error": "City not found or invalid API key"}

if __name__ == "__main__":
    city = input("Enter city name: ")
    weather = get_weather(city)
    
    print("\nWeather Information:")
    for key, value in weather.items():
        print(f"{key}: {value}")
