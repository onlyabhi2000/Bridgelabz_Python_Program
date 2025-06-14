"""
 Given the head of a singly linked list, write a program to reverse the linked list, and return the head pointer to the reversed list.
"""

##Approach -->

"""Initialize three pointers: prev, current, and next.

Traverse the list:

Save current.next into next.

Reverse the link: make current.next = prev.

Move prev and current one step ahead.

When done, prev will be the new head of the reversed list"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    prev = None            # Step 1: Previous node initially None (new tail)
    current = head         # Step 2: Start from the current head

    while current:
        next_node = current.next  # Step 3: Store the next node
        current.next = prev       # Step 4: Reverse the current node's pointer
        prev = current            # Step 5: Move prev one step forward
        current = next_node       # Step 6: Move current one step forward

    return prev  # Step 7: prev becomes the new head of the reversed list


# Function to print the list
class LinkedListUtils:

    @staticmethod
    def create_linked_list(arr):
        if not arr:
            return None
        head = Node(arr[0])
        current = head
        for val in arr[1:]:
            current.next = Node(val)
            current = current.next
        return head

    @staticmethod
    def print_linked_list(head):
        while head:
            print(head.data, end=" → " if head.next else "")
            head = head.next
        print("NULL")


# Driver code
head = LinkedListUtils.create_linked_list([1, 2, 3, 4, 5])
print("Original List:")
LinkedListUtils.print_linked_list(head)

reversed_head = reverse_linked_list(head)
print("Reversed List:")
LinkedListUtils.print_linked_list(reversed_head)
