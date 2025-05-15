string = "abhishek"
vowels = "aeiou"

count_v = 0
count_c = 0

for ele in string:
    if ele in vowels:
        count_v +=1
    else:
        count_c +=1

print(count_v , count_c)
    