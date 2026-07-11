class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

students = [
    Student("Alice",90),
    Student("Bob",80)
]

for s in students:
    print(s.name, s.marks)