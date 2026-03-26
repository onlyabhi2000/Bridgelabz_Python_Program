"""
Problem Statement: Given the root of a Binary Tree, return the height of the tree. 
The height of the tree is equal to the number of nodes on the longest path from root to a leaf.
"""

###Approcah1 :
"""
Start at the root.
Recursively calculate the height of left and right subtrees.
The height at a node is 1 + max(height of left, height of right).
"""
"""
Time & Space Complexity:
Time: O(n) — Each node is visited once.
Space: O(h) — Recursion stack, h is height of the tree.
"""

class NodeTree:
    def __init__(self , val):
        self.val = val
        self.left = None
        self.right = None

def get_tree_height(root):
    if root is None:
        return 0
    
    left_height = get_tree_height(root.left)
    right_height = get_tree_height(root.right)
    return 1+max(left_height,right_height)