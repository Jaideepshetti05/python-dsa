from collections import defaultdict


def subarray_sum(nums, k):
    d = defaultdict(int)
    d[0] = 1

    total = 0
    count = 0

    for num in nums:
        total += num
        count += d[total - k]
        d[total] += 1

    return count


nums = [1, 2, 3]
k = 3

print("Subarrays with sum k:", subarray_sum(nums, k))