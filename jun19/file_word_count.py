with open("sample.txt", "r") as file:
    data = file.read()

print("Words:", len(data.split()))