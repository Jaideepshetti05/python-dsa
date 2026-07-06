import json

student = {
    "name": "Jaideep",
    "age": 20,
    "course": "B.Tech"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

with open("student.json", "r") as file:
    data = json.load(file)

print(data)