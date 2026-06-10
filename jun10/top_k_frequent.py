from collections import Counter

nums = [1,1,1,2,2,3]
k = 2

result = Counter(nums).most_common(k)

print([num for num, freq in result])