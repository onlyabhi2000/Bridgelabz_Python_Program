#reduce : It returns a single reduce value 

#Syntax : 
# import functools
# functools.reduce(function_name , iterable


import functools

data = [1 ,2,4,5]
def sum(a,b):
    return a+b

reduce_obj = functools.reduce(sum , data)

print(reduce_obj)

