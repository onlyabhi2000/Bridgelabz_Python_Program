# Input : s = "5347"

# Output : "5347"

# Explanation : The odd numbers formed by given strings are --> 5, 3, 53, 347, 5347.

# So the largest among all the possible odd numbers for given string is 5347.


string = "5347"
sub_string  = []

for i in range(0 , len(string)):
    for j in range(i+1 , len(string)+1):
        if int(string[i:j])%2!=0:
            sub_string.append(string[i :j])



# str_to_int = int(sub_string)
print(sub_string)

new_int_string = []
for i in sub_string:
    new_int_string.append(int(i))


print("-->",new_int_string)
print(max(new_int_string))
