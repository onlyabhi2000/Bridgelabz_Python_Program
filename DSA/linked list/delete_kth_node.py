"""
Problem Statement: Given a linked list and an integer N, the task is to delete the Nth node from the end of the linked list and print the updated linked list.
"""
"""
Move the fast pointer k steps ahead.

Then move both fast and slow pointers one step at a time until fast reaches the end.

At that point, slow will be just before the node to delete.

Update slow.next to skip the target node.
Time complexity : O(n) 
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_kth_node(head, k):
    # Dummy node to handle edge cases easily
    """
    dummy = Node(0)
→ Creates a temporary new node (dummy node) with value 0. This node is not part of the original list.

dummy.next = head
→ The dummy node now points to the original head, so the list becomes: dummy → 1 → 2 → 3 → ...




    """
    dummy = Node(0)
    dummy.next = head

    fast = dummy
    slow = dummy

    # Move fast k+1 steps ahead
    for i in range(k + 1):
        if fast:
            fast = fast.next

    # Move both pointers until fast reaches the end
    while fast:
        fast = fast.next
        slow = slow.next

    # Remove the k-th node from the end
    if slow.next:
        slow.next = slow.next.next

    return dummy.next




## helper function--->
def create_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=" → " if head.next else "")
        head = head.next
    print("NULL")


arr = [1, 2, 3, 4, 5]
k = 2

head = create_linked_list(arr)
print("Original List:")
print_linked_list(head)

new_head = remove_kth_node(head, k)
print(f"After removing {k}th node from end:")
print_linked_list(new_head)
