nums = [10,5,8,20,15]

largest = second = float('-inf')

for n in nums:
    if n > largest:
        second = largest
        largest = n
    elif largest > n > second:
        second = n

print(second)nums = [10,5,8,20,15]

largest = second = float('-inf')

for n in nums:
    if n > largest:
        second = largest
        largest = n
    elif largest > n > second:
        second = n

print(second)