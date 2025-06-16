class TreeNode:
    def __init__(self , data):
        self.data = data 
        self.left = None
        self.right =None

def insert_node(root , value):
    new_node = TreeNode(value)
    if root is None:
        return new_node
    
    node_to_visit = [root] ##this is a list of nodes we still need to process ---->breadth-first search

    while node_to_visit :
        current_node = node_to_visit.pop()

        ## will check left subtree is empty hthn add it here
        if current_node.left is None:
            current_node.left = new_node
            return root
        else:
            # Otherwise, add the left child to the list to visit later
            node_to_visit.append(current_node.left)


        if current_node.right is None:
            current_node.right = new_node
            return root
        else:
             node_to_visit.append(current_node.right)
    return root



def print_tree_level_order(root):
    if not root:
        return
    nodes_to_visit = [root]
    while nodes_to_visit:
        node = nodes_to_visit.pop(0)
        print(node.data, end=' ')
        if node.left:
            nodes_to_visit.append(node.left)
        if node.right:
            nodes_to_visit.append(node.right)

# Build tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Before insertion:")
print_tree_level_order(root)

insert_node(root, 6)

print("\nAfter insertion:")
print_tree_level_order(root)



