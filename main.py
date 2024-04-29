import requests


api_key = "f5eccd1935e67301b2a710abbce7876b"

user_input = input("Enter City: ")


weather_data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q= {user_input}&units=Metric&appid={api_key}")

weather_location = user_input

weather_temp = weather_data.json()["main"]["temp"]
print(f"{weather_location}: Sıcaklık: {weather_temp} derece")



