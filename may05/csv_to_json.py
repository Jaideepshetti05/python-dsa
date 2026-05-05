import csv, json

data = []

with open("data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

print("Converted")