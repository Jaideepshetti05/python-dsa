def canJump(nums):
    maxReach = 0
    for i, num in enumerate(nums):
        if i > maxReach:
            return False
        maxReach = max(maxReach, i + num)
    return True