from collections import Counter

text="programming"

count=Counter(text)

for ch in text:
    if count[ch]==1:
        print(ch)
        break