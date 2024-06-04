import requests

import matplotlib.pyplot as plt

# The API key
api_key = "de4208bc2c280287b9df4c61ae3a87ba"

# URL for the OpenWeatherMap
api_url = 'http://api.openweathermap.org/data/2.5/weather?'

# Enter the city name for which you want to get the weather data
location = input("Enter city name: ")

all_url = f"{api_url}q={location}&appid={api_key}&units=metric" 

response = requests.get(all_url)

# Getting data in JSON format
data = response.json()
# print(data)

# Check if the city exists
if data['cod'] == '404':
    print("City not found.")

else:
    # Extracting weather data
    weather = data['main']
    temperature = weather['temp']
    humidity = weather['humidity']
    description = data['weather'][0]['description']
    wind_speed = data['wind']['speed']
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']

    # Printing weather data
    print(f"Weather in {location}: ")
    print(f"Temperature: {temperature}°C")
    print(f"Description: {description}")
    print(f"Humidity: {humidity}%")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")



# Plots a point on the map for the location
plt.scatter(longitude, latitude, color='red', label=f"{location}: {description}, {temperature}°C, {humidity}")

# Add labels and legend
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()

# Displays the data
plt.show()