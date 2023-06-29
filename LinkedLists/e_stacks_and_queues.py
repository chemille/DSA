# Implementation of a Stack
# We can use any linear data structure to implement a stack. 
# For example, using a linked list, we could implement a Stack class like this:

class Stack:

    def __init__(self):
        self.store = LinkedList()

    def push(self, item): # This method adds an item to the top of hte stack
        self.store.add_first(item)

    def pop(self): # This method removes and returnst he item on the top of the stack.
        return self.store.remove_first()

    def is_empty(self): # This method returns True if the stack is empty and false otherwise.
        return self.store.length() == 0

# A stack might also implement a peek method which returns, 
# but does not remove the item on top of the stack, and 
# a size method which returns the number of items currently on the stack.

# Queue Implementation Considerations
# Like a stack, a queue can be implemented several ways and the implementation 
# should be hidden from the user. One way would be to implement a queue with a 
# linked list like this:

class Queue:
    def __init__(self):
        self.store = LinkedList()

    def enqueue(self, item): # This method puts an item into the back of the queue.
        self.store.add_last(item)

    def dequeue(self): # This method removes and returns the item at the front of the queue.
        if self.is_empty():
            return None

        self.store.remove_first()

    def is_empty(self): # This method returns True if the queue is empty and false otherwise.
        return self.store.length() == 0
    
# Big-O of enqueue and dequeue for the above queue implementation:
    # If the Linked List has a tail reference and is a doubly linked list, 
    # then both enqueue and dequeue can be done in O(1) time. 
    # If there is no tail reference then enqueue should perform in O(n) time.