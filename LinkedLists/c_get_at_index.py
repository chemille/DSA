# Since LLs are not stored in continguous memory, most read and write operations will 
# require us to traverse the list, meaning we must follow the pointers to travel from 
# one node to the next. With a SLL, we also maintain a reference to the head node, so 
# all of our traversal will start at the head of the list. 

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None 
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_to_beginning(self, value):
        new_node = Node(value) # Create a new object
        new_node.next = self.head # Set the new_node's next field to reference the head
        self.head = new_node # Then, update the LL's head field to point at the new node
    
    # Method for returning the value at the given index for a SLL.
    def get_at_index(self, index):
        # The index count should start at 0 and the function should return None if there
        # are fewer nodes in the LL than the given index value.    
        if not self.head:
            return None
        
        current_index = 0 # Keeps track of where we are at in the list
        current_node = self.head # Keeps track of node and since the first node is at 0
        # in the head of the list, we set the current_node to self.head
        
        while current_node and current_index < index: # while current_node != None and current_index <index:
            current_node += 1
            current_node = current_node.next
        if current_index == index and current_node:
            return current_node.val
        return None

    # Time O(n), and space O(1)