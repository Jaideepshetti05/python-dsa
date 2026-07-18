arr = [10, 4, 90, 22, 35]

first = second = float('-inf')

for x in arr:
    if x > first:
        second = first
        first = x
    elif first > x > second:
        second = x

print(second)