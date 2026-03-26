## indexing  ->Indexing is how you reference rows and columns.

# You can access rows using .loc[] or .iloc[].



import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "Country": ["India", "USA", "UK", "Germany"]
}

df = pd.DataFrame(data)
print(df)

##get only specidied column

col1df = pd.DataFrame(data , columns=["Age"])
rowdf = pd.DataFrame
print(df["Age"][2])