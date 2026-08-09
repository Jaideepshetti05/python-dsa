def max_subarray(nums):
    current = nums[0]
    maximum = nums[0]

    for num in nums[1:]:
        current = max(num, current + num)
        maximum = max(maximum, current)

    return maximum


numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print("Maximum Subarray Sum:", max_subarray(numbers))