text = "cloud devops cloud aws"

words = text.split()

count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

print(count)