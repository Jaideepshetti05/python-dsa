def next_greater(arr):
    result = [-1] * len(arr)
    stack = []

    for i, value in enumerate(arr):
        while stack and value > arr[stack[-1]]:
            index = stack.pop()
            result[index] = value

        stack.append(i)

    return result


numbers = [4, 5, 2, 10, 8]

print(next_greater(numbers))