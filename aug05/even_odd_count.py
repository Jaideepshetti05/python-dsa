nums=[2,5,6,7,9,12]

even=sum(1 for i in nums if i%2==0)
odd=len(nums)-even

print("Even:",even)
print("Odd:",odd)