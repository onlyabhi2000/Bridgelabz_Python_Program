"""
Problem Statement: Given the heads of two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

Examples:

Input Format: 
(Pointer/Access to the head of the two linked lists)

num1  = 243, num2 = 564

l1 = [2,4,3]
l2 = [5,6,4]

Result: sum = 807; L = [7,0,8]
"""
# Node class to define a single linked list node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Corrected this (it was set to `next`, which is undefined)


# Solution class with method to add two numbers represented as linked lists
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = Node(0)  # Fixed: `None(0)` is invalid — should be Node(0)
        current = dummy
        carry = 0

        # Traverse both lists
        while l1 or l2:
            x = l1.data if l1 else 0
            y = l2.data if l2 else 0
            total = x + y + carry
            carry = total // 10  # Fixed: use 10, not 2 (base 10, not binary)
            current.next = Node(total % 10)
            current = current.next
            ## move in to next node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:
            current.next = Node(carry)

        return dummy.next




# Helper function to create a linked list from a Python list
def create_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for num in arr[1:]:
        current.next = Node(num)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    while head:
        print(head.data, end=" -> " if head.next else "")
        head = head.next
    print()


# Create two input linked lists: 342 and 465
l1 = create_linked_list([2, 4, 3])  # Represents number 342
l2 = create_linked_list([5, 6, 4])  # Represents number 465

# Call the addTwoNumbers method
solution = Solution()
result = solution.addTwoNumbers(l1, l2)

# Print the result
print("Result Linked List:")
print_linked_list(result)  # Should print: 7 -> 0 -> 8
