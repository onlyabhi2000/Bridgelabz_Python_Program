# 4. Question: Write a function that checks if a given word is a palindrome.

word = "dog"

if (word == word[::-1]):
    print("palindrom")
else:
    print("not a palindrome")