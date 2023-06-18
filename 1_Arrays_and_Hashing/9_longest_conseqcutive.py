'''Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 
Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
'''


def longestConsecutive(nums):

#### Brute force sorted ###
    # sorted_arr = sorted(set(nums))
    # count = 1
        
    # for i in range(len(sorted_arr)-1):
    #     if sorted_arr[i] + 1 == sorted_arr[i+1]:
    #         count += 1
    # return count

##### O(n) ######

    num_set = set(nums)
    max_length = 0
    
    for num in nums:
        if num - 1 not in num_set:  # Starting element of a sequence
            current_length = 1
            while num + 1 in num_set:
                num += 1
                current_length += 1
            max_length = max(max_length, current_length)
    
    return max_length



print(longestConsecutive([100,4,200,1,3,2])) #4
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1])) #9
