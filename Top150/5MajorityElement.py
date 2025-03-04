'''
Majority Element
Easy

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

Follow-up: Could you solve the problem in linear time and in O(1) space?
'''

def majorityElement(nums) -> int:
  ## My first solution O(n) time and space ##
  
    hash = {}

    for n in nums:
        if n not in hash:
            hash[n] = 1
        else:
            hash[n] += 1
    
    majority = (0,0)

    for key in hash:
        if hash[key] > majority[1]:
            majority = (key, hash[key])
    
    return majority[0]

  ## O(n) linear time and O(1) constant space solution ##

print(majorityElement([2,2,1,1,1,2,2])) # Output: 2
print(majorityElement([3,2,3])) # Output: 3

