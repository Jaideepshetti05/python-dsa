def topKFrequent(nums, k):

    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    sorted_freq = sorted(
        freq.items(),
        key=lambda x: x[1],
        reverse=True
    )

    top_k = sorted_freq[:k]

    return [num for num, count in top_k]


nums = [1,1,1,2,2,3]
k = 2

print(topKFrequent(nums, k))