import requests

# The API key
api_key = "de4208bc2c280287b9df4c61ae3a87ba"

# URL for the OpenWeatherMap
api_url = 'http://api.openweathermap.org/data/2.5/weather?'

# Enter the city name for which you want to get the weather data
location = input("Enter city name: ")

all_url = api_url + 'q=' + location + '&appid=' + api_key + '&units=metric' 

response = requests.get(all_url)

# Getting data in JSON format
data = response.json()
#print(data)

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

    # Printing weather data
    print("Weather in {}: ".format(location))
    print("Temperature: {}°C".format(temperature))
    print("Description: {}".format(description))
    print("Humidity: {}%".format(humidity))
    print("Wind Speed: {} m/s".format(wind_speed))
