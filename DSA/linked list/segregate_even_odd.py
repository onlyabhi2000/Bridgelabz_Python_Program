"""
Problem Statement : Segregate even and odd nodes in LinkedList

Given a LinkedList of integers. Modify the LinkedList in such a way that in Modified LinkedList all the even numbers appear before all the odd numbers in LinkedList.

Also, note that the order of even and odd numbers should remain the same. 

Examples:

Example 1:
Input: 1→2→3→4→5→6→Null
Output: 2→4→6→1→3→5→Null
Explanation : 
Odd Nodes in LinkedList are 1,3,5 and 
Even Nodes in LinkedList are 2,4,6
In Modified LinkedList all even Nodes comes before 
all Odd Nodes. So Modified LinkedList looks like 
2→4→6→1→3→5→Null. Order of even and odd Nodes is 
maintained in modified LinkedList.
"""


##approach--------------->
"""
Traverse the linked list once.

Maintain two separate lists:

One for even numbers.

One for odd numbers.

Attach the even list to the odd list.

Update the head to the start of the even list.
"""

# Define the Node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def segregateEvenOdd(self, head):
        # Create two lists: one for even, one for odd
        even_nodes = []
        odd_nodes = []

        # Traverse the linked list and separate even and odd nodes
        current = head
        while current:
            if current.data % 2 == 0:
                even_nodes.append(current.data)
            else:
                odd_nodes.append(current.data)
            current = current.next

        # Combine both lists: even first, then odd
        result_values = even_nodes + odd_nodes

        # If result is empty, return None
        if not result_values:
            return None

        # Create a new linked list from the result values
        new_head = Node(result_values[0])
        current = new_head
        for value in result_values[1:]:
            current.next = Node(value)
            current = current.next

        return new_head





# Function to create linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Function to print the linked list
def print_linked_list(head):
    while head:
        print(head.data, end=" → " if head.next else "")
        head = head.next
    print("NULL")


# Input list
arr = [1, 2, 3, 4, 5, 6]
head = create_linked_list(arr)

# Call the function
solution = Solution()
new_head = solution.segregateEvenOdd(head)

# Print result
print("Modified Linked List:")
print_linked_list(new_head)
