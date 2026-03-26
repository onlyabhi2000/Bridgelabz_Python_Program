"""
Selection sort is a sorting algorithm that selects the smallest element from an unsorted list in each iteration and places that element at the beginning of the unsorted list.
	Finds the minimum (or maximum) element from the unsorted part and swaps it to its correct position.
    Selection and one swap per pass.

"""

"""
Steps 1: First search the minimum value in the list use min() or
directly use assume the first index as the min value and compare it with every element and keep on chnaging th eminimuny element 

Step2 : Swap the smallest element at the first posistion of the array

Now the array have two part one is sorted which have the first element and unsorted part -rest of the lement , 
now agian assume the 2nd element as the minimum value and keep to repeating the same step
"""

size = int(input("enter the size of the array : "))
a = []
for i in range(size):
    val = int(input("Enter the value"))

    a.append(val)

print(a)


for i in range(0, size):
    min_index = i
    for j in range(i + 1, size):
        if a[j] < a[min_index]: 
            min_index = j
    a[i], a[min_index] = a[min_index], a[i]

print(a)


    