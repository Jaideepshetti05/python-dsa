sentence = "madam hello level civic python"

for word in sentence.split():
    if word == word[::-1]:
        print(word)