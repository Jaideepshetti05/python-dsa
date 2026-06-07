nums = [1, 2, 4, 5]
n = 5

expected = n * (n + 1) // 2
actual = sum(nums)

print("Missing Number:", expected - actual)