"""
Stack : A Stack is a linear data structure that follows a particular order in which the operations are performed.
The order may be LIFO (Last In First Out) or FILO (First In Last Out)
"""

class Stack:
    def __init__(self):
        self.items = []

    ## method to add an element into the stack
    def push(self, item):
        self.items.append(item)

    ## method to remove the top element from the stack
    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return None

    ## method to return the top element without removing it
    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return None

    ## method to get the size of the stack
    def size(self):
        return len(self.items)

    ## method to display the stack
    def print(self):
        return self.items
    
    def isEmpty(self):
        return len(self.items) == 0


# Example usage
stack_obj = Stack()

stack_obj.push('2')    
print(stack_obj.print())


stack_obj.push('3')    
print(stack_obj.peek())  

stack_obj.pop()    
print(stack_obj.print())  
print(stack_obj.size())       



"""
1. What are Infix, Prefix, and Postfix?
🔹 Infix Notation (Most Common - Human Style)
Operators are between operands

Example:

css
Copy
Edit
A + B
(A + B) * C
🔹 Prefix Notation (Polish Notation)
Operators are before the operands

Example:

css
Copy
Edit
+ A B
* + A B C
🔹 Postfix Notation (Reverse Polish Notation)
Operators are after the operands

Example:

css
Copy
Edit
A B +
A B + C *
"""