sentence = "cloud computing and devops engineering"

words = sentence.split()
largest = max(words, key=len)

print("Largest Word:", largest)