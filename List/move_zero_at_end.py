#move all zeros at the end 
# list = [1 , 3, 5 , 0 , 1 , 0 , 0 , 6]
# zeros_list =[]
# non_zero_list = []
# for i in list:
#     if i == 0:
#         zeros_list.append(0)
#     else:
#         non_zero_list.append(i)

# final_list = non_zero_list +zeros_list
# print(final_list)


#Second Way 

list1 = [1 , 3, 5 , 0 , 1 , 0 , 0 , 6]
for i in list1:
    if i ==0:
        list1.remove(i)
        list1.append(i)

print(list1)
