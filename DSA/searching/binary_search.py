"""
Binary Search :: 
Binary Search is a search algorithm that works by dividing a sorted list in half repeatedly to locate a target value.

Working ::-->
Look at the middle element.

If it matches the target, return its index.

If the target is smaller, search the left half.

If the target is larger, search the right half.

Repeat steps 1-4 until you find it or the range becomes empty.

"""

"""

"""

def bianry_search(arr , target):
    low = 0 
    high = len(arr)-1

    while low<= high:
        mid = (low+high)//2

        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid -1

    return f"{target} is not found"


arr = [1,2,5,7,9]

result=bianry_search(arr ,target=5 )

print(result)

