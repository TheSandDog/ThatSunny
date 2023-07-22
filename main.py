import requests
import math


# Function to create a line separator for printing
def create_line(length=50):
  print("-" * length)


api_key = '30d4741c779ba94c470ca1f63045390a'

# Get the user input for the city
create_line()

user_input = input("Enter city: ")

try:
  # Fetch weather data from the OpenWeatherMap API
  weather_data = requests.get(
      f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}"
  )
  weather_data.raise_for_status()  # Check for request errors
except requests.RequestException as e:
  # Handle any request exceptions and exit the program
  print("Error occurred while fetching weather data:", e)
  exit()

try:
  data = weather_data.json()
except ValueError as e:
  # Handle JSON parsing errors and exit the program
  print("Error occurred while parsing JSON data:", e)
  exit()

if data['cod'] == '404':
  print("No City Found")
else:
  # Extract relevant weather information from the API response
  weather = data['weather'][0]['main']
  description = data['weather'][0]['description']
  temp = round(data['main']['temp'])
  humidity = data['main']['humidity']
  wind_speed = data['wind']['speed']

  # Print the weather information in a formatted way
  create_line()
  print(f"The weather in {user_input} is: {weather} ({description})\n")

  print(f"The temperature in {user_input} is: ~{(math.ceil(temp))}ºF")

  temp_c = (temp - 32) * 5 / 9
  print(f"The temperature in {user_input} is: ~{(math.ceil(temp_c))}ºC\n")

  print(f"Humidity: ~{(math.ceil(humidity))}%\n")

  print(f"Wind Speed: ~{(math.ceil(wind_speed))}mph")

  wind_speed_kmh = wind_speed * 1.609344
  print(f"Wind Speed: ~{(math.ceil(wind_speed_kmh))}kph")

  create_line()
