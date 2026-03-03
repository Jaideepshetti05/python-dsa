def two_sum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return left, right
        elif s < target:
            left += 1
        else:
            right -= 1

print(two_sum([2,7,11,15], 9))