"""You are given:
A non-negative number in string form, like "1432219"
An integer k, which tells you how many digits you are allowed to remove
Your goal is:
👉 After removing exactly k digits, return the smallest possible number that you can make.
Input:
num = "1432219"
k = 3
output = "1219"
"""


def remove_k_elements(nums , k):
    stack = []

    for element in nums:
        while k >0 and stack and stack[-1]> element:
            stack.pop()
            k-=1
        stack.append(element) # Add current element

    ##if the elements still left to remove then will remove it from end 

    while k > 0:
        stack.pop()
        k-=1

    result = ''.join(stack).lstrip('0')

    return result if result else '0'

print(remove_k_elements(nums="1432219" , k=3))
        
    
