list = [1 , 2 , 2, 1]
reverse_list = []

for i in range(len(list)-1 , -1 , -1):
    reverse_list.append(list[i])

print(reverse_list)

if list == reverse_list:
    print("Palindrome")
    
else:
    print("Not a palindrome")