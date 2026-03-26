"""
Given a postfix expression, the task is to evaluate the postfix expression.
 A Postfix expression is of the form "a b operator" ("a b +") i.e., a pair of operands is followed by an operator.
 Examples:

Input: arr = ["2", "3", "1", "*", "+", "9", "-"]
Output: -4
Explanation: If the expression is converted into an infix expression, it will be 2 + (3 * 1) - 9 = 5 - 9 = -4.


"""

arr = ["2", "3", "1", "*", "+", "9", "-"]

stack = []
operators = set(['+', '-', '*', '/'])

for token in arr:
    if token not in operators:
        # Push operand as integer
        stack.append(int(token))
    else:
        # Pop last two operands
        b = stack.pop()
        a = stack.pop()

        if token == '+':
            res = a + b
        elif token == '-':
            res = a - b
        elif token == '*':
            res = a * b
        elif token == '/':
            res = int(a / b)  # integer division

        # Push result back to stack
        stack.append(res)

# Final result will be on top of stack
print(stack.pop())

