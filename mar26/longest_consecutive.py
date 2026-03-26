def longest_consecutive(nums):
    s = set(nums)
    longest = 0

    for num in s:
        if num - 1 not in s:
            length = 1
            while num + length in s:
                length += 1
            longest = max(longest, length)

    return longest

print(longest_consecutive([100,4,200,1,3,2]))