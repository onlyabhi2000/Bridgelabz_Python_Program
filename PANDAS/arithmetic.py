import pandas as pd

data =({"a": [1,2,3,4],
        "b": [5,6,7,8]})

df = pd.DataFrame(data=data)

df['c'] = df['a'] + df['b']
df['c'] = df['a'] - df['b']
print(df)

##condition based checking -True/False

data1 =({"a": [1,2,3,4],
        "b": [5,6,7,8]})

df2 = pd.DataFrame(data=data1)

df2[">3"] = df2["a"]>2

print(df2)


######Delete and insert and update function in pandas#####


##adding new column

df3 = pd.DataFrame(data=data)

#parameter(index no , index name , data)
df3.insert(1,'new_col' , [10,20,20,40])
print(df3)