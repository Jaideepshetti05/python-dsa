class Student:
    count = 0

    def __init__(self):
        Student.count += 1

Student()
Student()
Student()

print(Student.count)