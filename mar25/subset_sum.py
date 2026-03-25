def subset_sum(nums, target):
    dp = set([0])

    for num in nums:
        new_dp = dp.copy()
        for s in dp:
            new_dp.add(s + num)
        dp = new_dp

    return target in dp

print(subset_sum([3, 34, 4, 12, 5, 2], 9))
