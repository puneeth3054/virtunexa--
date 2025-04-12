import requests

# Replace with your actual API key from OpenWeatherMap
API_KEY = 'YOUR_API_KEY_HERE'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather_by_city(city_name):
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'
    }
    return fetch_weather(params)

def get_weather_by_coordinates(lat, lon):
    params = {
        'lat': lat,
        'lon': lon,
        'appid': API_KEY,
        'units': 'metric'
    }
    return fetch_weather(params)

def fetch_weather(params):
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        return {
            'city': data.get('name'),
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'description': data['weather'][0]['description'].capitalize()
        }
    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
        return None
    except KeyError:
        print("Unexpected response format.")
        return None

def main():
    print("Weather App")
    print("1. Search by city name")
    print("2. Search by coordinates")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        city = input("Enter city name: ")
        weather = get_weather_by_city(city)
    elif choice == '2':
        try:
            lat = float(input("Enter latitude: "))
            lon = float(input("Enter longitude: "))
            weather = get_weather_by_coordinates(lat, lon)
        except ValueError:
            print("Invalid coordinates.")
            return
    else:
        print("Invalid choice.")
        return

    if weather:
        print(f"\nWeather in {weather['city']}:")
        print(f"Description: {weather['description']}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")

if __name__ == "__main__":
    main()
