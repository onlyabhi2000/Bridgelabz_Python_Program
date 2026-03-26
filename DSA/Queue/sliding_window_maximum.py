"""Input: nums = [1,3,-1,-3,5,3,6,7], k = 3 → Output: [3,3,5,5,6,7]"""
"""Given an array nums and an integer k, return the maximum values in every sliding window of size k"""
"""
1. Given an array, find the maximum element in all subarrays of size k using a queue. This involves using a queue to track potential maximums.
"""

##Brute force approch
"""arr = [1,3,-1,-3,5,3,6,7]
k=3

n = len(arr)
if n*k ==0:
    print("array is empty")

if k==1:
    print(f"{arr}, have only one value")

result = []
for i in range(n-k+1):
    window_max = max(arr[i:i +k])
    result.append(window_max)

print(result)"""



## optimal approach using deque


from collections import deque

def max_sliding_window(nums, k):
    n = len(nums)
    if n * k == 0:
        return []

    result = []
    dq = deque()  # stores indices

    for i in range(n):
        # Remove indexes out of window
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove smaller elements in k range as they are useless
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        # Append max in window to result
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

k = 3
nums =  [3, 3, 5, 5, 6, 7]
print(max_sliding_window(nums, k))  