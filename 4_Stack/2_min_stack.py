''' 155. Min Stack
Medium

Design a stack that supports push, pop, top, and retrieving the minimum element in 
constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.


Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
'''

class MinStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # We know we have to support 4 operations, and we're going to have 2 stacks. 
        # So in our constructor, let's define the 2 stacks first. Initally empty arrays.
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # First operation is push
        # In our first stack, we're always going to take the input value and append it to the first stack.
        self.stack.append(val)
        # For second stack, we need to know if there is already a value inserted in the minStack,
        # Then, take the min of the input value and min of top value of minStack and get the min of those two
        # and append that value to the minStack. If self.minStack is non-empty we do this; otherwise, 
        # if self.minStack is empty, we take the min val of the two.
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        # For our pop function, we don't have to return antyhing. We just have to pop from both stacks.
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # To get top value of stack, we get the last value that was inserted in the first stack.
        # Since we're getting the last value when it's non-empty, it takes care of edge cases where stack is empty.
        return self.stack[-1]

    def getMin(self) -> int:
        # This will return from the top of the minStack. This also only gets called when stack is non-empty.
        return self.minStack[-1]

    ## Every one of these operations are done in O(1) time.


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

