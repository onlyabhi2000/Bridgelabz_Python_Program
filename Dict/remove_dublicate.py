dict = {'a': 1 , "b" : 2 , "c" : 1}

seen = set()
result = {}

for key , value in dict.items():
    if value not in seen:
        result[key]  = value
        seen.add(value)

print(result)