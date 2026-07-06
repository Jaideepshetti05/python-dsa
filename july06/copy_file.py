with open("input.txt", "r") as source:
    data = source.read()

with open("output.txt", "w") as destination:
    destination.write(data)

print("File copied successfully.")