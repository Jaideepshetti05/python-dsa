nums = [10,11,12,13,14,15]

even = sum(1 for i in nums if i % 2 == 0)
odd = len(nums) - even

print("Even:", even)
print("Odd:", odd)