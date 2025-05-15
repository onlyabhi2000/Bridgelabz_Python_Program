# Find the common elemnets in two list
list1 = [1,2,3, 5,7]

list2 = [3,5, 1, 8 ,9]

common_list = []

for i in list1:
    for j in list2:
        if i == j:
            common_list.append(i)
print(common_list)
            
