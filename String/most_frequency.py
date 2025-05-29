string = "aaabbcde"
dict = {}
for i in string:
    if i in dict:
        dict[i]+=1
    else :
        dict[i] = 1
for key , value in dict.items():
    max_count = max(dict , key = dict.get)
    result = dict[max_count]
print(max_count,result)

    