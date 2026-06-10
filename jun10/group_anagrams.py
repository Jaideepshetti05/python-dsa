from collections import defaultdict

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = defaultdict(list)

for word in words:
    groups["".join(sorted(word))].append(word)

print(list(groups.values()))