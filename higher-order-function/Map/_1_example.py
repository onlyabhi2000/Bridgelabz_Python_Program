# find the length of individuals name using map
names = ['abhi' , 'shek' , 'abhishek']

def name_length(name):
    return len(name)
mapped_obj = map(name_length,names)

print(list(mapped_obj))


# for ele in mapped_obj:
#     print(ele)

# print(mapped_obj)