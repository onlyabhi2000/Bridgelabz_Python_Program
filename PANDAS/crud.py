"""
A DataFrame is a table. It contains an array of individual entries, each of which has a certain value. Each entry corresponds to a row (or record) and a column.
"""

##CREATING DATAFRAME

import pandas as pd
##using dictionary
df = pd.DataFrame({" column1" : [20,30] , "column2" : [40 ,60]})
print(df)

df2 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['inex1' , 'index2'])

print(df2)

##using list
list = ['a' , 'b' , 'c'] 
df = pd.DataFrame(list)
print(df)


"""
Series
A Series, by contrast, is a sequence of data values. If a DataFrame is a table, a Series is a list. And in fact you can create one with nothing more than a list:
"""
pd.Series([1, 2, 3, 4, 5])


###------------------REQADING DATAFRAMES----------------------###

##read df from a csv
user_data = pd.read_csv("/home/abhishek/Desktop/BridgeLabz_Python_Mentor/PANDAS/sample_users.csv")



##We can use the shape attribute to check how large the resulting DataFrame is:

print(user_data.shape)

print(user_data.head())





