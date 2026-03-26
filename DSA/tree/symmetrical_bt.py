"""

Problem Statement: Given a Binary Tree, determine whether the given tree is symmetric or not.
 A Binary Tree would be Symmetric, when its mirror image is exactly the same as the original tree.
   If we were to draw a vertical line through the centre of the tree, the nodes on the left and right side would be mirror images of each other.
"""

class TreeNode:
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None

def is_symmerical(root):
    if root is None:
        return True
    
    def is_mirror(left,right):
        ##if no left sub treee and right subtree means symmetry
        if not left and not right:
            return True
        if not left or not right:
            return True
        if left.data!= right.data:
            return False
        
        ##recursively check outer or inner tree
        return is_mirror(left.left , right.right) and is_mirror(left.right ,right.left)
    return is_mirror(root.left , root.right)



##tree creation

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

root.right.left = TreeNode(4)
root.right.right = TreeNode(3)


print(is_symmerical(root))
    

