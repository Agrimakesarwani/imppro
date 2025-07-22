import requests

city = input("Enter a city: ")
api_key = "fd0f8c1f5859502331c92ff8b645225a"  # Replace this with your OpenWeatherMap API key

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Weather:", data["weather"][0]["description"].capitalize())
else:
    print("City not found.")