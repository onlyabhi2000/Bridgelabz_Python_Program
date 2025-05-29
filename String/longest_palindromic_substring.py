# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

string = "babad"

sub_string = []

for i in range(0 , len(string)):
    for j in range(i+1 , len(string)+1):
        sub_string.append(string[i:j])


print("sunstring", sub_string)


palindrome_list =[]

for s in sub_string:
    #shortcut --> keep in mind
    if s == s[::-1]:
        palindrome_list.append(s)

longest_pal = max(palindrome_list, key =len)

print("longest _substring is " , longest_pal)
# print(sub_string)