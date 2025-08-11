# In Python, the map() function is a built-in function used to apply a function to every item in an iterable 
# (like a list or tuple) and return a new iterable (a map object) with the results.
#map(function, iterable)





# find the length of individuals name using map
names = ['abhi' , 'shek' , 'abhishek']

def name_length(name):
    return len(name)

mapped_obj = map(name_length,names)

print(list(mapped_obj))


# for ele in mapped_obj:
#     print(ele)

# print(mapped_obj)