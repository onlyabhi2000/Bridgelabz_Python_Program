"""
Reverse a givem string using stack 
Example: "hello" ---> olleh
"""

string = "hello"
stack = []
for char in string:
    stack.append(char)

print(stack)

reversed_string = ""
while stack:
    reversed_string+=stack.pop()

print(reversed_string)