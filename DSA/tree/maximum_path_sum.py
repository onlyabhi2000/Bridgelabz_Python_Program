class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sum_of_path(root):
    max_sum = float('-inf')

    def dfs(node):
        nonlocal max_sum 

        if node is None:
            return 0

        # Get the maximum path sum from left and right, ignore negative paths
        left = max(0, dfs(node.left))
        right = max(0, dfs(node.right))

        # Path that goes through this node
        current_path = node.data + left + right

        # Update max_sum if current path is better
        max_sum = max(max_sum, current_path)

        # Return max one-sided path sum to parent
        return node.data + max(left, right)

    dfs(root)
    return max_sum


# Create the tree
root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(15)
root.left.left = TreeNode(-4)
root.left.right = TreeNode(-6)
root.left.left.left = TreeNode(28)
root.left.left.right = TreeNode(-22)
root.right.right = TreeNode(-25)
root.right.right.left = TreeNode(3)
root.right.right.right = TreeNode(4)

print("Max Path Sum:", sum_of_path(root))  # Expected Output: 51
