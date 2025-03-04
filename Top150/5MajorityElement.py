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
  
    # hash = {}

    # for n in nums:
    #     if n not in hash:
    #         hash[n] = 1
    #     else:
    #         hash[n] += 1
    
    # majority = (0,0)

    # for key in hash:
    #     if hash[key] > majority[1]:
    #         majority = (key, hash[key])
    
    # return majority[0]

  ## Boyer-Moore Majority Voting Algorithm --> https://www.geeksforgeeks.org/boyer-moore-majority-voting-algorithm/ ##
  ## This algorithm works on the fact that if an element occurs more than n / 2 times, 
  ## it means the remaining elements other than this would definitely be less than n / 2.
  ## First, choose a candidate from the given set of elements. 
  ## If it's the same as the candidate element, votes += 1. Otherwise, votes -= 1.
  ## If the votes become 0, select another new element as the new candidate. 
  ## O(n) time and O(1) space

      candidate = None
      votes = 0
      
      # Finding majority candidate
      for i in range(len(nums)):
          if (votes == 0):
              candidate = nums[i]
              votes = 1
          else:
              if (nums[i] == candidate):
                  votes += 1
              else:
                  votes -= 1
      count = 0
      
      # Checking if majority candidate occurs more than n/2 times
      for i in range(len(nums)):
          if (nums[i] == candidate):
              count += 1
              
      if (count > len(nums) // 2):
          return candidate
          

## Another O(n) time and O(1) space solution ##

  # candidate = None
  # votes = 0

  # for num in nums:
  #   if votes == 0:
  #     candidate = num

  #   if num == candidate:
  #     votes += 1
  #   else:
  #     votes -= 1
      
  # return candidate

print(majorityElement([2,2,1,1,1,2,2])) # Output: 2
print(majorityElement([3,2,3])) # Output: 3
print(majorityElement([2,3,3,5,3,3,3,2])) # Output: 3

