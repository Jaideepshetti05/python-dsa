import json

json_data = '''
{
    "name": "Rahul",
    "age": 21,
    "course": "BTech"
}
'''

student = json.loads(json_data)

print("Student Details")
print("----------------")
print("Name   :", student["name"])
print("Age    :", student["age"])
print("Course :", student["course"])