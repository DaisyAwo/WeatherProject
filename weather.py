import requests

API_KEY = "8ba088b74607eecbd64fefd4a85ef2b7"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()

    weather = data["weather"][0]["description"]

    temperature = round(data["main"]["temp"] - 273.15, 2)
    temperature_two = round((data["main"]["temp"] - 273.15) * 1.8 + 32, 2)

    print("Weather:", weather)
    print("Temperature:",temperature, "celsius")
    print("Temperature:", temperature_two, "fahrenheit")

else:
    print("Error! Please try again.")
