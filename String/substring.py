#Find all subtring in a list 

string = "abc"

list = []

for i in range(0,len(string)):
    for j in range(i+1,len(string)+1):
        list.append(string[i:j])
print(list)




# Example: string = "abc"
# Outer loop (i) goes from 0 to 2:
# When i = 0:

# j ranges from 1 to 3

# string[0:1] = 'a'

# string[0:2] = 'ab'

# string[0:3] = 'abc'

# When i = 1:

# j ranges from 2 to 3

# string[1:2] = 'b'

# string[1:3] = 'bc'

# When i = 2:

# j = 3

# string[2:3] = 'c'