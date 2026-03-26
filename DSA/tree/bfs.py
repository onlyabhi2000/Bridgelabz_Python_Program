## for graph

# def bfs(graph , startNode):
#     visited_node = []
#     queue = [startNode]

#     while queue:
#         currentNode = queue.pop()
#         visited_node.append(currentNode)

#         for neighbor in graph[currentNode]:
#             if neighbor not in visited_node:
#                 queue.append(neighbor)

#     return visited_node



## for tree
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bfs(root):
    if not root:
        return []

    visited_node = []         # Stores the visited node data
    queue = [root]            # Queue for BFS, initialized with root node

    while queue:
        currentNode = queue.pop(0)  # Pop from front for FIFO
        visited_node.append(currentNode.data)

        # Append left and right children to queue if they exist
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)

    return visited_node


# Construct a simple binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("BFS Traversal:", bfs(root))  # Output: [1, 2, 3, 4, 5]
