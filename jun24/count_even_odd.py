nums = [1,2,3,4,5,6,7,8]

even = sum(1 for n in nums if n % 2 == 0)
odd = len(nums) - even

print("Even:", even)
print("Odd:", odd)