#  Question: You are given a list of strings. Write a function to filter out all strings that are palindromes.

lst = ["madam", "hello", "racecar", "python", "level"]
result = []
for i in lst:
    reverse = i[::-1]
    if i == reverse:
        result.append(i)
print(result)