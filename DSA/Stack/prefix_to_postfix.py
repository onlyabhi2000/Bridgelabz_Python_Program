"""
General Algorithm Summary:
Start scanning prefix from right to left.

If it's an operand → push it to the stack.

If it's an operator:

Pop two elements from stack (they are operands)

Form a string: operand1 operand2 operator

Push it back to the stack.

Final element on stack is the postfix expression.
"""


def prefix_to_postfix(expression):
    stack = []
    operators = ['*', '+', '-', '/' , '^']

    # Traverse from right to left
    for symbol in reversed(expression.split()):
        if symbol not in operators:
            #it means it is an operand -- push to stack
            stack.append(symbol)
        else:

             # It's an operator → pop two operands
            op1 = stack.pop()
            op2 = stack.pop()
            new_exp = f"{op1} {op2} {symbol}"  # postfix format
            stack.append(new_exp)
    return stack[0]


expression = "* + A B C"
print(prefix_to_postfix(expression))



"""
def isOperator(c):
    return c in ['*', '+', '-', '/']

def prefix_to_postfix(expression):
    stack = []

    for symbol in reversed(expression):
        if isOperator(symbol):

            op1 = stack.pop()
            op2 = stack.pop()


            new_expr = op1 + " " + op2 + " " + symbol
            stack.append(new_expr)
        else:
            stack.append(symbol)

    return stack[-1]


expression = "+a/bc*d-"
result = prefix_to_postfix(expression)
print("Prefix:", expression)
print("Postfix:", result)
"""