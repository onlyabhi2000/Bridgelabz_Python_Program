# The Python zip() function is a built-in utility that combines elements from one or more iterables (like lists, tuples, or strings)
#  into a single iterator of tuples, pairing elements based on their corresponding positions or indices

# Syntax: zip(*iterables, strict=False)

name = ['Alice', 'Bob', 'Charlie']
age = [25, 30, 35]
zipped = zip(name, age)
print(list(zipped))  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]