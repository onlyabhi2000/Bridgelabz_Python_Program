"""
approach : We use recursion to pop elements until we reach the middle element.
Once we hit the middle, we skip pushing it back (thus deleting it), and restore the rest.
"""

def delete_middle(stack):
    def remove(stack, current, n):
        if current == n // 2:
            stack.pop()
            return
        top = stack.pop()
        remove(stack, current + 1, n)
        stack.append(top)

    n = len(stack)         
    remove(stack, 0, n)  

stack = [1, 2, 3, 4, 5]
delete_middle(stack)
print(stack)  # Output: [1, 2, 4, 5]
