"""
To convert, we:

Use a stack

Scan left to right

For each token:

If operand → push to stack

If operator → pop 2 operands from stack, combine in prefix style → push back
"""

def postfix_to_prefix(expression):
    stack = []
    operators = ['*', '+', '-', '/' , '^']

    # traverse from left to roight

    for symbol in expression.split():
        if symbol not in operators:
            stack.append(symbol)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            new_exp= f"{symbol} {op1} {op2}"
            stack.append(new_exp)
    return stack[0]


postfix = "A B + C *"
print("Postfix to Prefix:", postfix_to_prefix(postfix)) 
