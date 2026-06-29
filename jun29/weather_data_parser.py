import json

filename = "weather.json"

with open(filename, "r") as file:
    data = json.load(file)

print("Weather Report")
print("-" * 30)

print("City:", data["city"])
print("Temperature:", data["temperature"], "°C")
print("Humidity:", data["humidity"], "%")
print("Wind Speed:", data["wind_speed"], "km/h")
print("Condition:", data["condition"])