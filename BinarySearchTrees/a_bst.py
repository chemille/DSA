## Binary Search Trees ##
# The key reqs for this new data structure are:
    # 1. Maintain a list of items in order.
    # 2. Add and delete elements in better than O(n) time
    # 3. Find elements with an O(log n) time
    # 4. Serialize the list into a string or another data type that can be 
    #    written to a file, network, or database in O(n) time or better.
# If we maintain a list of items in order, an array will struggle to add and delete items 
# in less than O(n) time unless the element is added/deleted from the end of the array. 
# A linked list will require O(n) time for all 4 operations because it has to traverse the 
# sorted list to do anything.

# BST -> non-linear data structure.
# Each node in a BST has pointers to two other nodes in the data structure. 
# We refer to these pointers as the child nodes of the original parent node. 
# We label each of the parent node's two children as the left and right children or pointers.
# Collectively, we can refer to a parent node's children as siblings. 
# The parent node can be thought of as similar to the prev pointer in a DLL; however, 
# unlike a LL, tree nodes do not generally maintain a pointer to their parent/previous node.

# A BST's left and right child nodes are required to maintain special properties. 
# The left child must have a key that is less than the key of its parent node. 
# The right child must have a key that is greater than or equal to that of its parent node.

# We can create a TreeNode class to encapsulate a single element or node w/i a BST.
class TreeNode:
    def __init__(self, key, val = None): # None is an optional parameter, so the default value will be assigned to None. 
        if val is None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None
        
# Instantiating TreeNode and Tree Objects
TreeNode(8, 'M') # We pass in a key: 8 and value: M. 
# If we just instantiate with TreeNode(8), the value will default to None.
# In the code above, if val is None: val = key. Since the key is 8, val will be 8. 

# We can create a Tree to represent a full BST data structure. 
class Tree:
    def __init__(self):
        self.root = None # The root is the starting node in the Tree
    # Tree methods go here...        
        
Tree() # Instantiate a new empty Tree with no nodes to start off with.

