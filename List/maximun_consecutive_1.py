#Count Maximum Consecutive One's in the array

# problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array
# Example 1:

# Input: prices = {1, 1, 0, 1, 1, 1}

# list = [1, 1, 0, 1, 1, 1]

def max_one(list):
    count = 0
    count_max = 0

    for i in list:
        if i == 1:
            count+=1
            count_max = max(count_max,count)
        else:
            count =0
    return count_max
    
list = [1, 1, 0, 1, 1, 1]
print(max_one(list))