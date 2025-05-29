# remove dublicate from a string
string = "programming"
string_new = ""
for i in string:
    if i not in string_new:
        string_new +=i
print(string_new)