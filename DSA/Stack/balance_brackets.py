class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return None
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def peek(self):
        if self.items:
            return self.items[-1]
        return None
    
    def print(self):
        return self.items


def balance_parenthesis(expression):
    ## if expression length is odd, it's not balanced
    if len(expression) % 2 != 0:
        return False
    
    opening = set('({[')
    pairs = set([('(',')'), ('{','}'), ('[',']')])

    stack_obj = Stack()

    for bracket in expression:
        if bracket in opening:
            stack_obj.push(bracket)
        else:
            popped = stack_obj.pop()
            if (popped, bracket) not in pairs:
                return False
                
    return stack_obj.isEmpty()


# Test
expression = '{[())]}'
print(balance_parenthesis(expression))  



"""
Steps:
Loop through each character in the expression.

If it’s an opening bracket ((, {, [), push it to the stack.

If it’s a closing bracket (), }, ]):

Pop the top of the stack.

Check if the popped item matches the corresponding opening bracket.

At the end, if the stack is empty, the expression is balanced."""