"""
Linear Search :: 
Linear Search checks each element of the array one by one until:

It finds the target value, or

It reaches the end of the list (if the value isn't there)

works on the unsorted array also 
"""

def linear_search1(arr , target):
    for i in range(len(arr)):
        if arr[i] == target:
            return f"{target} element found at index no {i}" ## found element --return index
    return f"{target} is not present"
    

arr = [2, 1, 5, 8, 9,3,7]
target = 4
result = linear_search1(arr , target)
print(result)

