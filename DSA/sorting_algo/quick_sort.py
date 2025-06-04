"""Quick Sort  Algorithm ---> 
An array is divided into subarrays by selecting a pivot element (element selected from the array).
While dividing the array, the pivot element should be positioned in such a way that elements less than pivot are kept on the left side and elements greater than pivot are on the right side of the pivot.
The left and right subarrays are also divided using the same approach. This process continues until each subarray contains a single element.
At this point, elements are already sorted. Finally, elements are combined to form a sorted array.
"""


def quick_sort(arr):
    if len(arr) <= 1:
        return arr 

    pivot = arr[-1]  # Choose the last element as pivot
    left = []     
    right = []      
    for i in range(len(arr) - 1):  # Exclude the pivot itself
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    # # Recursively sort left and right, then combine with pivot
    return quick_sort(left) + [pivot] + quick_sort(right)


a = [10, 5, 3, 8, 2]
sorted_a = quick_sort(a)
print("Sorted array:", sorted_a)
