import csv

filename = "sales.csv"

total = 0

highest = 0
top_product = ""

with open(filename, newline="") as file:

    reader = csv.DictReader(file)

    for row in reader:

        product = row["Product"]
        sales = float(row["Sales"])

        total += sales

        if sales > highest:
            highest = sales
            top_product = product

print("Total Sales:", total)
print("Highest Selling Product:", top_product)
print("Highest Revenue:", highest)