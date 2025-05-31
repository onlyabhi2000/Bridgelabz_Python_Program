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
