from collections import Counter


text = """
python java python cloud devops java
python cloud docker java python
"""

words = text.lower().split()

frequency = Counter(words)

for word, count in frequency.most_common():
    print(f"{word}: {count}")