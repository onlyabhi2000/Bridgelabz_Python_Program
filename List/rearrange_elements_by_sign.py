# Rearrange the elements of the list by its sign by preserving the order also 
# Problem Statement:

# There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements. Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.

# Note: Start the array with positive elements.

# Examples: 

# Example 1:

# Input:
# arr[] = {1,2,-4,-5}, N = 4
# Output:
# 1 -4 2 -5



list1 = [1, 2, -6 , 4,-7,-9]
p_list = []
n_list = []
final_list =[]

for i in list1:
    if i<=0:
        n_list.append(i)
    else:
        p_list.append(i)


for p , n in zip(p_list,n_list):
    final_list.append(p)
    final_list.append(n)

print(final_list)

print("p_list",p_list)
print("n_list",n_list)



#expected output  -- > [1 , -6 ,2 ,-7 , 4 ,-9]

#cheatcode 

# for a, b in zip(listA, listB):
#     # a comes from listA, b from listB
#     # do something with a and b
