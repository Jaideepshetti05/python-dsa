arr = [1, 2, 3, 5, 6, 7]

n = len(arr) + 1

expected = n * (n + 1) // 2
actual = sum(arr)

print("Missing Number:", expected - actual)