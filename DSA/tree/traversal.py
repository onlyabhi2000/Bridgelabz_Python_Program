## traversal

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right




def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)



def preorder(node):
    if node:
        print(node.data, end = '')
        preorder(node.left)
        preorder(node.right)


def postorder(node):
    if node :
        postorder(node.left)
        postorder(node.right)
        print(node.data , end = '')



##driver code

# Creating a binary tree:
#        1
#       / \
#      2   3
#     / \
#    4   5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder:")
inorder(root)  
print("\nPreorder:")
preorder(root)   

print("\nPostorder:")
postorder(root)  
