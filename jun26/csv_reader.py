import csv

with open("students.csv") as file:
    reader = csv.reader(file)

    for row in reader:
        print("Name:", row[0], "Marks:", row[1])