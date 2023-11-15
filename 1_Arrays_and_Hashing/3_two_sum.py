'''TWO SUM
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''

def two_sum(nums, target):
    # Approach 1 # ENUMERATE function

    # lookup = {}  
    # for index, n in enumerate(nums):
    #     second_num = target - n
    #     if second_num in lookup:
    #         return[lookup[second_num],index]
    #     lookup[n] = index  
    # return 

    # Approach # 2 # hash map #
    # mapping value to index in hashmap
    
    # lookup = {}
    # for i in range(len(nums)):
    #   second_num = target-nums[i]
    #   if second_num in lookup:
    #     return(lookup[second_num], i)
    #   lookup[nums[i]] = i
    # return 
    
    
    # # Both solutions: time O(n) -> n is len of nums list, iterates through list once, performing constant time operations for each element. 
    # ## Space O(n) -> dictionary stores n key-value pairs, resulting in O(n) space. 

    ## Approach 3 is also O(n) time and space. Worst case scenario, you have to loop through the entire list.

    hash_map = {}
    
    for i, j in enumerate(nums):
        second_num = target - j
        if second_num in hash_map:
            return [i, hash_map[second_num]]
        hash_map[j] = i
        
print(two_sum([3,4,1], 0)) # []
print(two_sum([2,7,11,15], 9)) # [0,1]
print(two_sum([3,2,4], 6)) # [1,2]
print(two_sum([3,3], 6)) # [0,1]
