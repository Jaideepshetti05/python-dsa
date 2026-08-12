def two_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        total = arr[left] + arr[right]

        if total == target:
            return left, right
        elif total < target:
            left += 1
        else:
            right -= 1

    return None


numbers = [1, 2, 4, 6, 8, 9]
print(two_sum(numbers, 10))