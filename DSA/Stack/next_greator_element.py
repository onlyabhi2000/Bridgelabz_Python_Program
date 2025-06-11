"""
Given an array of integers, for each element, find the next greater element to its right. If no greater element exists, return -1 for that position.
input --> arr = [4, 5, 2, 10]  || output ----> [5, 10, 10, -1]
"""

def next_greater_elements(arr):
    n = len(arr)
    result = [-1] * n  
    stack = []         

    #Traverse from right to left
    for i in range(n - 1, -1, -1):
        # Remove all elements <= current element
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        
        # If stack not empty, top is the next greater
        if stack:
            result[i] = stack[-1]
        
        # Push current element to stack
        stack.append(arr[i])

    return result


arr = [4, 5, 2, 10]
print(next_greater_elements(arr))


