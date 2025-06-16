class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def dfs(root):
    if not root:
        return []

    visited_node = []       # Stores visited node data
    stack = [root]          # Stack for DFS (LIFO)

    while stack:
        currentNode = stack.pop()        # Pop last inserted node
        visited_node.append(currentNode.data)

        # Push right first so that left is processed first (preorder)
        if currentNode.right:
            stack.append(currentNode.right)
        if currentNode.left:
            stack.append(currentNode.left)

    return visited_node



# Construct a simple binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("DFS Traversal:", dfs(root))  # Output: [1, 2, 4, 5, 3]
