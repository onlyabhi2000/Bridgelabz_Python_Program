# Example: "aaabbcc" → "a3b2c2"

string = "aaabbcc"
dict = {}

for i in string:
    if i in dict :
        dict[i] +=1

    else:
        dict[i] =1

# print(dict)

new_string = ""

for key , value in dict.items():
    new_string+=key+str(value)


print(new_string)

