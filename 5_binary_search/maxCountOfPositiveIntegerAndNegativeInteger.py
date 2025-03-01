''' NOT PART OF THE ROADMAP, BUT LISTED ON LEETCODE AS AN EASY BINARY SEARCH PROBLEM

2529. Maximum Count of Positive Integer and Negative Integer
Easy
Hint
Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
Note that 0 is neither positive nor negative.

Example 1:
Input: nums = [-2,-1,-1,1,2,3]
Output: 3
Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.

Example 2:
Input: nums = [-3,-2,-1,0,0,1,2]
Output: 3
Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.

Example 3:
Input: nums = [5,20,66,1314]
Output: 4
Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.
 
Constraints:
1 <= nums.length <= 2000
-2000 <= nums[i] <= 2000
nums is sorted in a non-decreasing order.
 
Follow up: Can you solve the problem in O(log(n)) time complexity?
'''

def maximumCount(nums) -> int:
    ## O(n) time nad O(1) space solution ##
    # posCount = 0
    # negCount = 0

    # for n in nums:
    #     if n < 0:
    #         negCount += 1
    #     elif n > 0:
    #         posCount +=1

    # return max(posCount, negCount)

    ## Binary search O(log n) time and O(1) spaxe solution ##
    posCount = 0
    negCount = 0

    if (nums[0] > 0 and nums[-1] > 0) or (nums[0] < 0 and nums[-1] < 0):
        return len(nums)

    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2
        if nums[m] > 0:
            r = m - 1
            posCount = len(nums) - m
        else:
            l = m + 1
    
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2
        if nums[m] < 0:
            negCount = m + 1
            l = m + 1
        else:
            r = m - 1
        
    return max(posCount, negCount)
        
print(maximumCount([-2,-1,-1,1,2,3])) #3
print(maximumCount([-3,-2,-1,0,0,1,2])) #3 
print(maximumCount([5,20,66,1314])) #4
print(maximumCount([-1563,-236,-114,-55])) #4
print(maximumCount([-1563,-236,-114,-55,427,447,687,752,1021,1636])) # 6
