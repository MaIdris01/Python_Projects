# import pyowm

# # Replace 'YOUR_API_KEY' with your actual API key
# owm = pyowm.OWM('de4208bc2c280287b9df4c61ae3a87ba')

# # Enter the city name for which you want to get weather data
# city = input("Enter city name: ")

# try:
#     observation = owm.weather_at_place(city)
#     w = observation.get_weather()

#     # Weather details
#     print("Weather in {}: ".format(city))
#     print("Temperature: {}°C".format(w.get_temperature('celsius')['temp']))
#     print("Description: {}".format(w.get_detailed_status()))
#     print("Humidity: {}%".format(w.get_humidity()))
#     print("Wind Speed: {} m/s".format(w.get_wind()['speed']))

# except pyowm.exceptions.api_response_error.NotFoundError:
#     print("City not found.")





import requests

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'de4208bc2c280287b9df4c61ae3a87ba'

# Base URL for the OpenWeatherMap API
base_url = 'http://api.openweathermap.org/data/2.5/weather?'

# Enter the city name for which you want to get weather data
city = input("Enter city name: ")

# Construct the complete URL with parameters
complete_url = base_url + 'q=' + city + '&appid=' + api_key + '&units=metric'

# Sending HTTP request to the OpenWeatherMap API
response = requests.get(complete_url)

# Getting data in JSON format
data = response.json()

# Check if the city is found
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
    print("Weather in {}: ".format(city))
    print("Temperature: {}°C".format(temperature))
    print("Description: {}".format(description))
    print("Humidity: {}%".format(humidity))
    print("Wind Speed: {} m/s".format(wind_speed))
