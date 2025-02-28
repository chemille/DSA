'''
Find Minimum in Rotated Sorted Array (medium)
You are given an array of length n which was originally sorted in ascending order. 
It has now been rotated between 1 and n times. 
For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Notice that rotating the array 4 times moves the last four elements of the array to the beginning. 
Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Example 1:
Input: nums = [3,4,5,6,1,2]
Output: 1

Example 2:
Input: nums = [4,5,0,1,2,3]
Output: 0

Example 3:
Input: nums = [4,5,6,7]
Output: 4

Constraints:
1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000

Recommended Time & Space Complexity
You should aim for a solution with O(logn) time and O(1) space, where n is the size of the input array.
'''

def findMin(nums) -> int:
    ## O(n) time and O(1) space solution ##
    # return min(nums)

    ## Neetcode binary search solution ##
    ## Note that this algorithm, nums[m] >= nums[l], only works on a rotated array
    ## If nums[m] >= nums[l], search to the right. Otherwise, search to the left.
    ## O(log n) time, O(1) space

    lowest = nums[0]
    l, r = 0, len(nums) - 1

    while l <= r:
        ## If the array is already sorted
        if nums[l] < nums[r]:
            lowest = min(lowest, nums[l])
            break

        ## Else if not sorted
        m = (l+r) // 2
        lowest = min(lowest, nums[m])   

        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1

    # return lowest   

    ## Another Neetcode binary search solution (lower bound)
    ## O(log n) time, O(1) space

    # l, r = 0, len(nums) - 1

    # while l < r:
    #     m = l + (r - l) // 2
    #     if nums[m] <= nums[r]:
    #         r = m
    #     else:
    #         l = m + 1 
    # return nums[l]
     
print(findMin([3,4,5,6,1,2])) #1
print(findMin([4,5,0,1,2,3])) #0
print(findMin([4,5,6,7])) #4
