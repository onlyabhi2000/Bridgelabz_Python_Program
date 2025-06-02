"""
Why Linked Lists?
Linked lists were created to overcome various drawbacks associated with storing data in regular lists and arrays, as outlined below:

Ease of insertion and deletion
In lists, inserting or deleting an element at any position other than the end requires shifting all the subsequent items to a different position. This process has a time complexity of O(n) and can significantly degrade performance, especially as the list size grows. If you aren’t already familiar with how lists work or their implementation, you can read our tutorial on Python lists.

Linked lists, however, operate differently. They store elements in various, non-contiguous memory locations and connect them through pointers to subsequent nodes. This structure allows linked lists to add or remove elements at any position by simply modifying the links to include a new element or bypass the deleted one.

Once the position of the element is identified and there is direct access to the point of insertion or deletion, adding or removing nodes can be achieved in O(1) time.
"""

"""
resources : https://www.datacamp.com/tutorial/python-linked-lists
https://chatgpt.com/share/683d5eb2-47dc-8012-bc53-7c958c22a00b

"""


class Node :
    def __init__(self,data):
        self.data =data  ## Assigns the given data to the node
        self.next = None ## Initialize the next attribute to null

class Linkedlist:
    def __init__(self):
        self.head = None

        """By setting self.head to None, we are stating that the linked list is initially empty and that there are no nodes in the list to point to.
        We will now proceed to populate the list by inserting new nodes."""



    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)  # Create a new node 
        new_node.next = self.head  # Next for new node becomes the   current head
        self.head = new_node # Head now points to the new node

## note : https://chatgpt.com/share/683d5eb2-47dc-8012-bc53-7c958c22a00b
    def insertAtEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None:    
            self.head = new_node
            return
        last = self.head      
        while last.next:       
            last = last.next
        last.next = new_node 





    ## method to display the llist

    def printList(self):
        temp = self.head # Start from the head of the list
        while temp:
            print(temp.data,end=' ') # Print the data in the current node
            temp = temp.next # Move to the next node
        print()  # Ensures the output is followed by a new line



    def deleteFromBeginning(self):
        if self.head is None:
            return "the list is empty"
        self.head = self.head.next

    def delelteFromEnd(self):
        if self.head is None:
            return "List is empty"
        
        ##if only one node is available
        if self.head.next is None:
            self.head = None
            return
            
        # Case 2: More than one node — traverse to second last node
        current = self.head
        while current.next.next:
            current = current.next

          # Now current is at second last node
        current.next= None

    ##methos to search an element

    def search(self,value):
        current = self.head
        position = 0
        while current :
            if current.data == value:
                return f"element {value} found at position {position}"
            current = current.next
            position+=1
        return f"element is not present"




    # def insert(self,data):
    #     new_node = Node(data)
    #     new_node.next = self.head
    #     self.head = new_node


##Driver code

list_obj =Linkedlist()

list_obj.insertAtBeginning('1')
list_obj.insertAtEnd('2')
list_obj.insertAtEnd('3')
list_obj.insertAtEnd('4')

presult =list_obj.printList()
print(presult)


list_obj.delelteFromEnd()

presult =list_obj.printList()
print(presult)

search_result = list_obj.search('2')
print(search_result)

