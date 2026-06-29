students = {}

n = int(input("Number of Students: "))

for _ in range(n):

    name = input("Name: ")
    marks = float(input("Marks: "))

    students[name] = marks

average = sum(students.values()) / len(students)

topper = max(students, key=students.get)

passed = len([m for m in students.values() if m >= 40])

print("\nAverage:", round(average, 2))
print("Topper:", topper, "-", students[topper])
print("Pass Percentage:", round((passed / n) * 100, 2), "%")