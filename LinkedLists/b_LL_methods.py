class Node:
    def __init__(self, value):
        self.val = value
        self.next = None # The next attribute for a new node is set to None by default.
        # This doesn't indicate that our node doesn't reference or link to another node.
        
# Creating a LinkedList class
# A separate LL class will be create to allow us to store the head of our LL.
# The rest of the list will be accessible via the head node. 

class LinkedList:
    def __init__(self):
        self.head = None # Our constructor initializes head to None so that when a new 
        # LinkedList instance is instantiated, we are creating an empty list.
        
    # We can create several methods which allow users to perform operations on or pull
    # info out of hte LL. Below are severak possible methods our class amy have:
    
    # This method adds a new node with the specific data value to the beginning of LL.
    def add_first(self, value):
        new_node = Node(value) # create a new node
        new_node.next = self.head # set the new node's next field
        self.head = new_node # update the LL's head field o point at the new node
        
        # Notice that since we are adding to the front of the list, the new_node's next attribute 
        # should always point ot the current (soon to be former) head of the list. 
    
    # Another method that returns the value in the first node in the LL. Returns None if empty.
    def get_first(self):
        if self.head is None:
            return None
        return self.head.val