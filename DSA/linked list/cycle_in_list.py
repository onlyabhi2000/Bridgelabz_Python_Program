"""Detech a cycle in a  ll , if presnet return true else False"""

## approach , use floyd's cycle detection techniques , use of slow and fast pointer , if they same at any point means there is a cycle

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True ## cycle detected 
        
    return False ## cycle not detected 



# ###
# # Helper to create normal list (no cycle)
# def create_linked_list(arr):
#     head = Node(arr[0])
#     current = head
#     for val in arr[1:]:
#         current.next = Node(val)
#         current = current.next
#     return head

# head = create_linked_list([1, 2, 3, 4, 5])
# print("Cycle Detected:", cycle(head))  # ➤ False



# Create a cycle manually
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

head.next = second
second.next = third
third.next = fourth
fourth.next = second  # Creating cycle (loop to second)

print("Cycle Detected:", cycle(head))  # ➤ True