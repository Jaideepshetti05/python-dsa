import csv

with open("students.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["ID","Name"])
    writer.writerow([1,"John"])

print("CSV Created")