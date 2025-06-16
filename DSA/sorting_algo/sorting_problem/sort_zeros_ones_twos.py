"""
Given an array arr[] consisting of only 0s, 1s, and 2s. The task is to sort the array, i.e., put all 0s first, then all 1s and all 2s in last.

Examples:

Input: arr[] = {0, 1, 2, 0, 1, 2}
Output: {0, 0, 1, 1, 2, 2}
Explanation: {0, 0, 1, 1, 2, 2} has all 0s first, then all 1s and all 2s in last.
"""

## Solution 1
arr = [0, 1, 2, 0, 1, 2]
# zeros = []
# ones = []
# twos= []

# for i in arr:
#     if i == 0:
#         zeros.append(i)
#     elif i ==1:
#         ones.append(i)
#     else:
#         twos.append(i)

# result = zeros +ones+twos
# print(result)






"""We use three pointers:

low: points to the next position for 0

mid: the current element being checked

high: points to the next position for 2"""
low = 0
mid = 0
high = len(arr)-1

while mid <= high:
    if arr[mid] == 0:
        arr[low], arr[mid] = arr[mid], arr[low]
        low += 1
        mid += 1
    elif arr[mid] == 1:
        mid += 1
    else:
        arr[mid], arr[high] = arr[high], arr[mid]
        high -= 1

print(arr)

