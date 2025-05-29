list = ['a' , 'd' , 'a' , 'f' , 'd']

freq ={}

for i in list :
    if i in freq:
        freq[i]+=1
    else:
        freq[i] =1

print(freq)