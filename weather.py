import requests
import tkinter as tk
from tkinter import messagebox

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return
    
    api_key = "19cda350ebf30a6d0d6e52fd0963dcb0"  # Replace with your OpenWeatherMap API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data["cod"] != 200:
            messagebox.showerror("Error", f"City not found: {city}")
            return
        
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        
        result_label.config(text=f"Temperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to retrieve weather data: {e}")

# GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

tk.Label(root, text="Enter City:").pack(pady=10)
city_entry = tk.Entry(root)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()
