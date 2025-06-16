def balance_parenthesis(expression):
    ## if expression length is odd, it's not balanced
    if len(expression) % 2 != 0:
        return False
    
    opening = set('({[')
    pairs = set([('(',')'), ('{','}'), ('[',']')])

    stack_obj = []

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