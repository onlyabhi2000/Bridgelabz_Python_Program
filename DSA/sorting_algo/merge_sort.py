""" MERGE SORT ====>
An array is divided into subarrays by selecting a pivot element (element selected from the array).

While dividing the array, the pivot element should be positioned in such a way that elements less than pivot are kept on the left side and elements greater than pivot are on the right side of the pivot.
The left and right subarrays are also divided using the same approach. This process continues until each subarray contains a single element.
At this point, elements are already sorted. Finally, elements are combined to form a sorted array.

"""


"""
Worst Case Complexity [Big-O]: O(n2)
Best Case Complexity [Big-omega]: O(n*log n)
"""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: already sorted

    # Step 1: Split the array into two halves
    mid = len(arr) // 2
    
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Step 2: Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # Step 3: Merge while comparing elements
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Step 4: Add remaining elements (if any)
    result.extend(left[i:])
    result.extend(right[j:])
    return result


a = [5, 2, 8, 1, 3]
sorted_a = merge_sort(a)
print("Sorted array:", sorted_a)
