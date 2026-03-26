# Question: How do you deep copy an object in Python?
## show an example of copy vs deepcopy


## copy ==> whenever we use copy tp copy an object , it created the reference of the object and chnage in the coped object leads to change the original object also

lst = [1,4,5]
copy_lst = lst
# copy_lst = lst.copy()
# print(copy_lst)

## will chnage the copied list
copy_lst.append(9)
print(copy_lst)
print(lst)  ## here originl lst will get change 

## if we use copy method the for outer list it creats a new object in memory but if nested list  is there thn for inner object it reference to same old object

## example

lst2 = [[2,3],[5,5]]
shallow_copy = lst2.copy()

# shallow_copy[0].append(1)    ## in this case original object will also get modified
shallow_copy.append(9)  ## here original lst will get chnage
print(shallow_copy)
print(lst2)


### Deepcopy -> in deepcopy a new memory is allocated for the copied object - not going to affect the original object if copied object is modified