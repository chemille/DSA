# Node class represents individual elements of a LL

# Defines a node in a SLL
# Node class encapsulates each individual elem of the LL. 
# It is comprised of an attribute that stores data and an attribute taht stores
# a reference to the next node in the chain. 
# Node class represents individual elems of a LL.

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None # The next attribute for a new node is set to None by default.
        # This doesn't indicate that our node doesn't reference or link to another node.
        
# We can create a new node element by passing in the data we want to store 
# to the node class constructor as follows.
node = Node(42)
print(node.val)

# We can update new_node to instead point at a second node by updating the value of its next
# attribute to reference the second node.
node_two = Node(84)
node.next = node_two
print(node_two.val)

# Similarly, we can update the value of a node by updating its val attribute.
node.val = "dog"
print(node.val)

# Since the Node class has been defined previously, we can create 
# individual nodes with the desired values:
node1 = Node(111)
node2 = Node(536)
node3 = Node(986)
node4 = Node(763)

# Then, Connect the nodes together to form the linked list by 
# updating the next attribute of each node:
node1.next = node2
node2.next = node3
node3.next = node4

# To print the linked list, iterate through the nodes and print the values:
current_node = node1
while current_node is not None:
    print(current_node.val)
    current_node = current_node.next

