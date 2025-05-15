#Union of Two Sorted Arrays
list1 = [1,2,3,4,7]
list2 = [1,2,4,5,6,7]
union_list = []
for i in list1:
    for j in list2:
        if i ==j:
            union_list.append(i)
print(union_list)
