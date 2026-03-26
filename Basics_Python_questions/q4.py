# How can you remove duplicates from a list?

list = [1,2,3,4,1]

print(set(list)) ## one way

result = []

for i in list:
    if i not in result:
        result.append(i)
print(result)


### if new list or se is not allowed

