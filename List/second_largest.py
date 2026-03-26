list = [1, 3,2,6,8,4]
largest = list[0]
second_largest = list[0]

for i in range(len(list)):
    if list[i] > largest :
        largest = list[i]

for i in range(len(list)):
    if list[i] > second_largest and list[i] != largest :
        second_largest = list[i]
print(second_largest)




# Your solution has two separate loops, and each loop iterates through the entire list once.”

# First loop → O(n)

# Second loop → O(n)

# So total time complexity is:

# O(n + n) = O(2n)

# In Big-O notation, we ignore constants, so the final time complexity is:

# O(n)