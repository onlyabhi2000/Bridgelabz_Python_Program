"""
Step-by-Step Logic:
Initialize an empty stack and a result list span[]

Loop through each day i:

While stack is not empty and price[stack[-1]] <= price[i]:

Pop from stack

If stack is empty:
→ All previous prices are ≤ current → span = i + 1

Else:
→ span = i - stack[-1] (distance from last higher price)

Push current index i to stack

Time: O(n) — each element is pushed/popped at most once

Space: O(n) for the stack and output


"""

def calculate_span(price):
    n = len(price)
    span = [0] * n
    stack = []

    for i in range(n):
        # Pop all prices smaller or equal to current price
        while stack and price[stack[-1]] <= price[i]:
            stack.pop()

        # If stack is empty, all previous prices were smaller
        if not stack:
            span[i] = i + 1
        else:
            span[i] = i - stack[-1]

        # Push current index to stack
        stack.append(i)

    return span



price = [100, 80, 60, 70, 60, 75, 85]

print(calculate_span(price))

