class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


###sum of nodes
def sum_of_nodes(root):
    if root is None:
        return 0
    else:
        leftSum = sum_of_nodes(root.left)
        rightSum = sum_of_nodes(root.right)
        return root.data + leftSum +rightSum
    
### height/depth of nodes
def height_of_nodes(root):
    if root is None:
        return 0
    else:
        leftHeight = height_of_nodes(root.left)
        rightHeight = height_of_nodes(root.right)

        return 1 +max(leftHeight,rightHeight)

##count of nodes 

def count_nodes(root):
    if root is None:
        return 0
    else:
        leftCount = count_nodes(root.left)
        rightCount = count_nodes(root.right)

        return 1 + leftCount +rightCount



##create a tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.right = TreeNode(6)

# Test the function
total_sum = sum_of_nodes(root)
print("Sum of all nodes:", total_sum)

total_height = height_of_nodes(root)

print("heigt is :", total_height)

nodes_count = count_nodes(root)
print("toatal nodes :", nodes_count)