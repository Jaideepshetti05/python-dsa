import json

data = {"name": "Jaideep", "course": "Cloud"}

with open("data.json", "w") as file:
    json.dump(data, file)

with open("data.json", "r") as file:
    print(json.load(file))