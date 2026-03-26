#1. Question: Write a function that takes a list of numbers and returns the sum.




def sum_of_list(num_list):
    total =0
    for i in num_list:
        total = total+i
    return total

num_list=[1,5,6,2,7]
print(sum_of_list(num_list))
    