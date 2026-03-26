"""
Problem Statement: Given the head of a linked list of integers, determine the middle node of the linked list.
However, if the linked list has an even number of nodes, return the second middle node.
"""
from reverse_linkedlist import LinkedListUtils


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


##methd to return the middle element 
# def find_middle_node(head):
#     # Initialize both pointers at the start of the list
#     slow = head
#     fast = head

#     # Traverse the list
#     while fast and fast.next:
#         slow = slow.next           # Move slow by 1 node
#         fast = fast.next.next      # Move fast by 2 nodes

#     # When fast reaches the end, slow is at the middle
#     return slow



   ##method to delete the  middle element
def delete_middle_node(head):
    # Edge case: If list is empty or has only one node
    if not head or not head.next:
        return None  # List becomes empty

    # Initialize pointers
    slow = head             # Will move one step at a time
    fast = head             # Will move two steps at a time
    prev = None             # Will track node before slow

    # Traverse the list to find middle
    while fast and fast.next:
        prev = slow             # Save the node before middle
        slow = slow.next        # Move slow 1 step
        fast = fast.next.next   # Move fast 2 steps

    # Delete the middle node by skipping it
    prev.next = slow.next

    # Return head of the updated list
    return head





### helper function

# Create linked list from a list
# def create_linked_list(arr):
#     if not arr:
#         return None
#     head = Node(arr[0])
#     current = head
#     for val in arr[1:]:
#         current.next = Node(val)
#         current = current.next
#     return head

# # Print linked list
# def print_linked_list(head):
#     while head:
#         print(head.data, end=" → " if head.next else "")
#         head = head.next
#     print("NULL")


head = LinkedListUtils.create_linked_list([1, 2, 3, 4, 5])
LinkedListUtils.print_linked_list(head)
# middle = find_middle_node(head)
# print("Middle Node:", middle.data)

delete_middle = delete_middle_node(head)
LinkedListUtils.print_linked_list(head)
