def max_consecutive_ones(nums):
    count = 0
    max_count = 0

    for n in nums:
        if n == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0

    return max_count


arr = [1,1,0,1,1,1]
print(max_consecutive_ones(arr))