sentence = "Python programming language is amazing"

words = sentence.split()

print(max(words, key=len))