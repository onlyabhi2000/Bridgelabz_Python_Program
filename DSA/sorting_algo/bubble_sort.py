"""  
compares adjacent element and  if a[j] < a[j+1] then swap the elements 
Time Complexity : O(n2)

"""
size = int(input("enter the size of the array : "))
a = []
for i in range(size):
    val = int(input("Enter the value"))

    a.append(val)

print(a)

for i in range(size):
    for j in range(0, size - i - 1):
        if a[j]> a[j+1]:
            a[j] , a[j+1] = a[j+1] , a[j]

print("Sorted array using bubble sort is:", a)


