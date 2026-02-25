def subarraySum(nums, k):
    count = 0
    prefix = 0
    hashmap = {0:1}

    for num in nums:
        prefix += num
        if prefix - k in hashmap:
            count += hashmap[prefix-k]
        hashmap[prefix] = hashmap.get(prefix,0) + 1
    return count

print(subarraySum([1,1,1],2))