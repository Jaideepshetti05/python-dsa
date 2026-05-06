file = open("sample.txt", "r")

text = file.read()

words = text.split()

print("Total Words:", len(words))

file.close()