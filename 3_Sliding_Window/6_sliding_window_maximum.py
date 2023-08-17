"""239. Sliding Window Maximum
Hard

You are given an array of integers nums, there is a sliding window of size k 
which is moving from the very left of the array to the very right. You can only 
see the k numbers in the window. Each time the sliding window moves right by one 
position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""
from collections import deque
import collections

def maxSlidingWindow(nums, k):
    # ## My solution ## works for smaller inputs, but time limit exceeded for larger inputs
    # # edge cases
    # if len(nums) <= 1:
    #     return nums
    
    # # Initialize an empty array to append max from each window
    # # Use pointers to keep track of window
    # # left pointer and right pointer + k - 1
    # # Iterate through nums and check each window to grab max
    
    # result = []
    # l = 0
    
    # for r in range(len(nums)-k+1):
    #     r += k - 1
    #     result.append(max(nums[l:r+1]))
    #     l += 1
        
    # return result
    
    ## Time complexity O(k * (n-k)), where k is the size of window and n is the length of the entire input
    ## minus k because that's how many windows we're going to have. 
    
    
    
    
    ## Solution using deque for better efficiency ##
    # if len(nums) <= 1:
    #     return nums

    # result = []
    # window = deque()  # Create a deque to store indices of elements within the current window

    # # Process the first k elements separately to initialize the deque
    # for i in range(k):
    #     while window and nums[i] >= nums[window[-1]]:
    #         window.pop()
    #     window.append(i)

    # # Process the remaining elements using the sliding window approach
    # for i in range(k, len(nums)):
    #     result.append(nums[window[0]])  # The front of the deque holds the maximum for the current window

    #     # Remove elements that are out of the current window
    #     while window and window[0] <= i - k:
    #         window.popleft()

    #     # Remove elements that are smaller than the current element
    #     while window and nums[i] >= nums[window[-1]]:
    #         window.pop()

    #     window.append(i)  # Add the current element's index to the deque

    # result.append(nums[window[0]])  # Append the maximum for the last window

    # return result

    ## O(n) time complexity because each element can only be added to the deque once, which means
    ## the deque is limited to n pushes. Every iteration of the while loop uses l pop, which means 
    ## the while loop will not iterate more than n times int otal, across all iterations of the for
    ## loop. Worst case scenario, every element will be pushed and popped once, giving a time 
    ## complexity of O(2*n) --> O(n).
    ## Space complexity is O(k) as the size of the deque can grow a max up to a size of k.



    ## Another solution using deque and while loop ##
    # res = []
    # left = right = 0
    # q = deque()
    
    # while right < len(nums):
    #     # While there is data in q, and current value is greater than last value in deque
    #     while q and nums[right] > nums[q[-1]]:
    #         # Pop the index from deque
    #         q.pop()
    #     # Add current index, which is right, to the deque    
    #     q.append(right)    
    #     print(right, q)
        
    #     # Edge case
    #     # If left pointer is greater than fist item in deque
    #     if left > q[0]:
    #         # Pop from left of deque
    #         q.popleft()
        
    #     # Check length of current sliding window and if it's greater than or equal to k
    #     if right + 1 >= k:
    #         # Add value to res
    #         res.append(nums[q[0]])
    #         # Shift left pointer
    #         left += 1
    #     # Shift right pointer
    #     right += 1
        
    # return res
    
    
    
    ## NeetCode's solution O(n) ##
    output = []
    q = collections.deque()
    l = r = 0
    
    while r < len(nums):
        # while q is not empty and the topmost value or right most value in our queue is less than the 
        # current value we are inserting. So while smaller values exist is our queue
        while q and nums[q[-1]] < nums[r]:
            # We want to remove
            q.pop()
        # Then we can add the new value to our queue
        q.append(r) # adding index to because we can easily get the value associated to that index
        
        # This is a bit of an edge case.
        # If left value is out of bounds ofo ur window, we want to remove it from the window.
        # If left index is greater than the left most value in our queue
        if l > q[0]:
            # Remove from queue
            q.popleft()
            
        # Our window is at least size k
        if (r + 1) >= k:
            # Add the left most which is also the max in our queue to the output array
            output.append(nums[q[0]])
            # Update left pointer (only gets udpated when our window is at least size k)
            l += 1
        # Right pointer gets updated with each iteration
        r += 1
        
    return output

print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)) # [3,3,5,5,6,7]
print(maxSlidingWindow([1], 1)) # [1]

# Notes:
# Deque in Python
# Deque (Doubly Ended Queue) isp referred over a list in cases where we need quick append and pop operations
# from both endso f the container, as deque provides an O(1) time for append and pop operations as compared
# to a list that provides O(n) time complexity.

# Types of Restricted Deque Input
# Input Restricted Deque:  Input is limited at one end while deletion is permitted at both ends.
# Output Restricted Deque: output is limited at one end but insertion is permitted at both ends.

# # Example code:
# from collections import deque
# # Declaring deque
# q = deque([11,7,45,8])
# print(q)

# # Import collections for deque operations
# import collections 
# # Initializing deque
# dq = collections.deque([1,2,3])
# # Use append() to insert element at right end
# dq.append(9)
# # User appendleft() to insert element at left end
# dq.appendleft(6)
# # Use pop() to delete element from right end
# dq.pop()
# # Use popleft() to delete element from left end
# dq.popleft()
# print(dq)