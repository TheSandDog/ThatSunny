import requests
import math
import tkinter as tk
from PIL import Image, ImageTk


# Function to create a line separator for printing
def create_line(length=50):
  return "-" * length


def fetch_weather():
  api_key = '30d4741c779ba94c470ca1f63045390a'
  user_input = city_entry.get()

  try:
    # Fetch weather data from the OpenWeatherMap API
    weather_data = requests.get(
      f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}"
    )
    weather_data.raise_for_status()  # Check for request errors
  except requests.RequestException as e:
    # Handle any request exceptions and update the output label
    output_label.config(
      text=f"Error occurred while fetching weather data: {e}")
    return

  try:
    data = weather_data.json()
  except ValueError as e:
    # Handle JSON parsing errors and update the output label
    output_label.config(text=f"Error occurred while parsing JSON data: {e}")
    return

  if data['cod'] == '404':
    output_label.config(text="No City Found")
  else:
    # Extract relevant weather information from the API response
    weather = data['weather'][0]['main']
    description = data['weather'][0]['description']
    temp = round(data['main']['temp'])
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    # Update the output label with weather information
    output_label.config(
      text=f"The weather in {user_input} is: {weather} ({description})\n\n"
      f"The temperature in {user_input} is: ~{math.ceil(temp)}ºF\n\n"
      f"The temperature in {user_input} is: ~{math.ceil((temp - 32) * 5 / 9)}ºC\n\n"
      f"Humidity: ~{math.ceil(humidity)}%\n\n"
      f"Wind Speed: ~{math.ceil(wind_speed)}mph\n\n"
      f"Wind Speed: ~{math.ceil(wind_speed * 1.609344)}kph")


# Create the main application window
app = tk.Tk()
app.title("Weather Information")

# Set the window to fullscreen
app.attributes("-fullscreen", True)

# Load the background image
bg_image = Image.open("assets/background.png")
bg_image = bg_image.resize((app.winfo_screenwidth(), app.winfo_screenheight()))
bg_image_tk = ImageTk.PhotoImage(bg_image)

# Create a label to display the background image
background_label = tk.Label(app, image=bg_image_tk)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create widgets for user input and output
city_label = tk.Label(app,
                      text="Enter city:",
                      font=("Helvetica", 18),
                      bg="white")
city_label.pack(pady=5)

city_entry = tk.Entry(app, font=("Helvetica", 16))
city_entry.pack()

get_weather_button = tk.Button(app,
                               text="Get Weather",
                               font=("Helvetica", 14),
                               command=fetch_weather)
get_weather_button.pack(pady=10)

output_label = tk.Label(app,
                        text="",
                        font=("Helvetica", 16),
                        wraplength=400,
                        bg="white")
output_label.pack()

# Start the Tkinter main loop
app.mainloop()
