"""
Given a Binary Tree, the task is to check if the given binary tree is a Binary Search Tree or not. If found to be true, then print "YES". Otherwise, print "NO".
"""

"""🧮 Algorithm:
Start with the full range (-∞, ∞)

For each node:

Check: min < node.val < max

Recurse left: (min, node.val)

Recurse right: (node.val, max)

If all nodes satisfy the range condition → It's a BST

"""


class Node:
    def __init__(self , val) :
        self.val = val
        self.left = None
        self.right = None


def is_bst(node , min_val = float('-inf') , max_val = float('inf')):
    if not node:
        return True ##node == None ➡️ there’s no node here (null branch) So not node becomes True || An empty subtree is always a valid BST
 

    if not(min_val < node.val < max_val):
        return False
    return (is_bst(node.left , min_val, node.val) and  is_bst(node.right , node.val , max_val ))


def check_bst(root):
    if is_bst(root):
        return True
    else:
        return False
    

root1 = Node(10)
root1.left = Node(5)
root1.right = Node(15)
root1.left.left = Node(2)
root1.left.right = Node(7)
root1.right.right = Node(20)

print("Test 1:", "YES" if check_bst(root1) else "NO")  

root2 = Node(10)
root2.left = Node(5)
root2.right = Node(15)
root2.left.left = Node(2)
root2.left.right = Node(12)

print("Test 2:", "YES" if check_bst(root2) else "NO") 