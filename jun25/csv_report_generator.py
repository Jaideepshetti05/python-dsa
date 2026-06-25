import csv

filename = "students.csv"

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["ID", "Name", "Marks"])
    writer.writerow([101, "Alice", 91])
    writer.writerow([102, "Bob", 84])
    writer.writerow([103, "Charlie", 95])

print("CSV File Created Successfully!\n")

with open(filename, "r") as file:
    reader = csv.reader(file)

    print("Student Report")
    print("-" * 30)

    for row in reader:
        print("\t".join(row))