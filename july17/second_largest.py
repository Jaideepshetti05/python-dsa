arr = [12,8,45,66,23]

first = second = float('-inf')

for x in arr:
    if x > first:
        second = first
        first = x
    elif first > x > second:
        second = x

print(second)