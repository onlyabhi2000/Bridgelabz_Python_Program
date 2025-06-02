"""
The properties that separate a binary search tree from a regular binary tree is---->

All nodes of left subtree are less than the root node
All nodes of right subtree are more than the root node
Both subtrees of each node are also BSTs i.e. they have the above two properties
"""


class Node:
    def __init__(self, data, left = None , right = None):
        self.data = data
        self.left = left
        self.right = right

class BST():
    def __init__(self):
        self.root = None

    ##Insert a node

    def insert(self, data):
        self.root = self.insert_recursion(self.root , data)

    def insert_recursion(self,node, data):
        pass



