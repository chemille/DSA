'''
11. Container With Most Water
Medium
25.4K
1.4K
Companies
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''


def maxArea(height) -> int:
    # Use 2 pointers, one at starting at left and one at end on the right side
    start = 0
    end = len(height) - 1

    greatest_area = 0

    while start < end:
        # In order to get the area of a rectangle, formula is length * height
        # The length would be the end - start 
        length = end - start
        # For the height, need to get the lower between height[start] and height[end]
        # because the lower point is up to where we can fill the water without overflowing
        greatest_area = max(greatest_area, length * min(height[start], height[end]))
        # Now we need to move the pointers 
        if height[start] < height[end]:
            # shift start pointer to right
            start += 1
        else:
            # or shift end pointer to left
            end -=1
    # This greatest_area will be updated as it goes through the iterations
    return greatest_area 

print(maxArea([1,8,6,2,5,4,8,3,7])) #49
print(maxArea([1,1])) # 1
