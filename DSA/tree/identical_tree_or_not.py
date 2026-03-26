class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def are_identical(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.data != root2.data:
        return False

    return are_identical(root1.left, root2.left) and are_identical(root1.right, root2.right)

# -------------------------------
# Create First Tree
#       1
#      / \
#     2   3
#    /
#   4

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)

# Create Second Tree (Identical)
#       1
#      / \
#     2   3
#    /
#   4

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)

# Test
result = are_identical(root1, root2)
print(result)
