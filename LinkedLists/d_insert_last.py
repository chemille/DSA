'''Implement a method add_last that inserts a new node with a given value as the new last 
node of the singly linked list.
'''

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_first(self, value):
        new_node = Node(value) # Create a new object
        new_node.next = self.head # Set the new_node's next field to reference the head
        self.head = new_node # Then, update the LL's head field to point at the new node

    def add_last(self, value):
        #write your code here#
        if not self.head: # if the list is empty
            self.add_first(value) # add value first to beginning of list
            return 
        
        new_node = Node(value)
        current = self.head
        
        while current.next: # while current.next is not None
        # we continue to iterate through list 
            current = current.next
            
        current.next = new_node
        
        
#This method will require us to combine our skills of traversing linked lists with 
# redirecting some of the nodes' pointers.

# Start by creating the new node with the value passed in.

# The ultimate goal for this function is to redirect the current last node in the list 
# to point at the new last node in the list.

# Consider how you might handle the edge case in which the list is empty.

# In the nominal case, where the list already has some number of nodes, consider using 
# a current pointer to find the last node in the list. Recall that the last node in the 
# list will have a next pointer with a None value.