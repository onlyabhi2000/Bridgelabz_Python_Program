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
