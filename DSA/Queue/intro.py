# A queue is a linear data structure that operates on the First-In, First-Out (FIFO) principle. 
# This means the first element added to the queue is the first element removed.

"""
Operations associated with queue are: 

Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition – Time Complexity : O(1)
Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty,
then it is said to be an Underflow condition – Time Complexity : O(1)
Front: Get the front item from queue – Time Complexity : O(1)
Rear: Get the last item from queue – Time Complexity : O(1)

"""


"""
Practical Applications --------------->
Task Scheduling: Used by operating systems for managing processes ready to execute or awaiting specific events.
Handling of Requests: Servers in multi-threaded environments queue multiple user requests, processing them in arrival order.
Data Buffering: Supports asynchronous data transfers between processes, such as in IO buffers and pipes.
Breadth-First Search: Employed in graph algorithms, like BFS, to manage nodes for exploration.
Order Processing: E-commerce platforms queue customer orders for processing.
Call Center Systems: Incoming calls wait in a queue before connecting to the next available representative.
"""






class Queue:
    def __init__(self):
        self.queue = []

    def enque(self,element):
        self.queue.append(element)
    
    def deque(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.queue.pop(0)
        
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def front(self):
        return self.queue[0]
    
    def rear(self):
        return self.queue[-1]
    
    def display(self):
        return self.queue


    ##reverse the using stack 
    #remove elemmet from queue and push it into stack
    #pop elemmet from stack and push it into queue

    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    def reverse_queue(self):
        stack = []
        while not self.isEmpty():
            stack.append(self.deque())
        while stack:
            self.enque(stack.pop())
        return self.queue




##driver code

queue = Queue()


queue.enque(1)
queue.enque(2)
queue.enque(3)
queue.enque(4)
queue.enque(5)


queue.deque()


print(queue.front())
print(queue.rear())

print(queue.display())


print(queue.reverse_queue())

