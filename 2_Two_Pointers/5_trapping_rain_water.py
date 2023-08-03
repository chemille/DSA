'''
42. Trapping Rain Water
Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.


Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array 
[0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
'''

def trap(height) -> int:
    # Initialize result = 0
    result = 0
    # Create pointers left = 0, right = len(height) - 1
    left = 0
    right = len(height) - 1
    # Keep track of highest values of height for the left and right
    left_highest = height[0]
    right_highest = height[-1]
    # Iterate through height so that it meets in the middle and stops 
    while left < right:
        # If the currentleft value is greater than left_highest,
            # left_highest is updated to the current left value
        # If the current right value is greater than the right_highest,
            # right_highest is updated to the current right value
        if height[left] > left_highest:
            left_highest = height[left]
        if height[right] > right_highest:
            right_highest = height[right]
        # If the left_highest is less than or equal to to the right_highest:
            # result += left_highest - height[start]
            # shift left pointer by + 1
        if left_highest <= right_highest:
            result += left_highest - height[left]
            left += 1
        # Otherwise, if the right_highest <= left_highest
            # result += right_highest - height[right]
            # shift right pointer by - 1
        else:
            result += right_highest - height[right]
            right -= 1
    # Return units of rain water being trapped (in blue)
    return result

# time O(n) -> iterating through each to find max left and right 
# space O(1) -> not creating additional data structures

## Neetcode solution ##
    # result = 0
    # left, right = 0, len(height) - 1
    # left_highest, right_highest = height[left], height[right]

    # while left < right:
    #     if left_highest < right_highest:
    #         left += 1
    #         left_highest = max(left_highest, height[left])
    #         result += left_highest - height[left]
    #     else:
    #         right -= 1
    #         right_highest = max(right_highest, height[right])
    #         result += right_highest - height[right]
    # return result        
    
# time O(n), space O(1)

print(trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(trap([4,2,0,3,2,5])) # 9

    