class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

students = [
    Student("A", 90),
    Student("B", 82)
]

for s in students:
    print(s.name, s.marks)