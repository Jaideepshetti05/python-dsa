from collections import Counter

text = "python java python programming java python"

words = text.split()
frequency = Counter(words)

for word, count in frequency.items():
    print(word, ":", count)