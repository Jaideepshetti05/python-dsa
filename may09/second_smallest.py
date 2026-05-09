nums = list(map(int, input("Enter numbers: ").split()))

smallest = min(nums)

nums.remove(smallest)

print("Second Smallest:", min(nums))