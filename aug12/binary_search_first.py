def first_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    answer = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            answer = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return answer


numbers = [1, 2, 2, 2, 4, 5]

print("First occurrence:", first_occurrence(numbers, 2))