import json

student = {
    "name": "Rahul",
    "age": 21,
    "course": "Cloud Computing"
}

with open("student.json", "w") as file:
    json.dump(student, file)

with open("student.json", "r") as file:
    data = json.load(file)

print(data)