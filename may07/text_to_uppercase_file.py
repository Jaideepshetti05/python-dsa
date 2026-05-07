with open("input.txt", "r") as file:
    text = file.read()

with open("output.txt", "w") as file:
    file.write(text.upper())

print("Converted to uppercase")