# File: sliding_window_max.py
from collections import deque

def maxSlidingWindow(nums, k):
    dq, res = deque(), []
    for i, n in enumerate(nums):
        while dq and nums[dq[-1]] < n:
            dq.pop()
        dq.append(i)
        if dq[0] == i - k:
            dq.popleft()
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res

print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))