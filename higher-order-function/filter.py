#Syntax --> filter_obj = filter(function , iterable)
#Filetr : is an higher order function is used to filter out the elements of iterbales

#Example 

data = [1 ,4, 6,3, 7, 77,31 ]


def filter_even(val):
    if val%2==0:
        return True
    
filtered_obj=filter(filter_even , data)
print(list(filtered_obj))
