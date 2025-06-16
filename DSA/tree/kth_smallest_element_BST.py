

""" Brute Force Solution
Approach:
Perform in-order traversal (Left → Root → Right).

This will give us sorted values from the BST.

Return the element at index k-1.

Time Complexity:
O(N) where N = number of nodes (to traverse all nodes)

Space: O(N) for storing the list
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest_brute_force(root, k):
    def in_order(node):
        if not node:
            return []
        return in_order(node.left) + [node.val] + in_order(node.right)

    sorted_values = in_order(root)
    print(sorted_values)
    return sorted_values[k - 1]


##Optimal solution --->

"""Optimal Solution
Approach:
Use in-order traversal but with a counter.

Stop traversing once we find the kth smallest value.

Avoid storing all values.

Time Complexity:
Still O(H + k) in average case (H = height of tree)

Better space efficiency: O(H) recursion stack, no list needed"""


def kth_smallest_optimal(root ,k):
    stack = []
    current = root

    while True :
        while current:
            stack.append(current)
            current= current.left

        current= stack.pop()

        k-=1 #We are essentially counting how many nodes we've visited so far in sorted order.

        if k == 0:
            return current.val #Return the value of the kth smallest node. The function ends here.
        current= current.right #If k != 0, we now move to the right child of the current node.
        





##driver code-->


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)

print(kth_smallest_brute_force(root, 3))

print(kth_smallest_optimal(root , 4))
