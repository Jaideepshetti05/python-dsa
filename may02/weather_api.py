import requests

api = "https://api.open-meteo.com/v1/forecast?latitude=12.97&longitude=77.59&current_weather=true"
data = requests.get(api).json()

print(data['current_weather'])