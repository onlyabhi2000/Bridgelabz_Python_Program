# In Python, the map() function is a built-in function used to apply a function to every item in an iterable 
# (like a list or tuple) and return a new iterable (a map object) with the results.
#map(function, iterable)


"""map() applies a function to every element of an iterable and returns a map object.

## Syntax 

map_object = map(function_name , iterable)"""


# find the length of individuals name using map
names = ['abhi' , 'shek' , 'abhishek']

def name_length(name):
    return len(name)

# mapped_obj = map(name_length,names)
mapped_obj=map(lambda name:len(name),names)

print(list(mapped_obj))


# for ele in mapped_obj:
#     print(ele)

# print(mapped_obj)