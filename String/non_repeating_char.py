# find first non repeating character
string = "aabbcde"
dict = {}

for i in string:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i]+=1

for key , value in dict.items():
    if(value == 1):
        print(key , value)
        break



