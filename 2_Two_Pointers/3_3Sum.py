'''3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''

def threeSum(nums):

    ####### NeetCode solution #######
    res = [] # result will be returned as a list of lists
    nums.sort()

    # iterate through and use each num as possible first value
    for i, val in enumerate(nums):
        # we don't want to use the same value in the same position twice
        if i > 0 and val == nums[i - 1]: # val == nums[i-1] means it's the same value as before 
            # which we don't want to reuse the same value twice, so we continue to the next 
            continue
        # Use 2-pointer to solve the remainder 
        l, r = i + 1, len(nums) - 1 # r pointer is the end of the list
        
        while l < r: #  left cannot equal right, indices cannot be the same
            # compute threeSum
            threeSum = val + nums[l] + nums[r]
            # if the sum is too big
            if threeSum > 0:
                # then, we decrease our right pointer so it shifts to the left
                r -= 1
            # on the other hand, if the sum is too small
            elif threeSum < 0:
                # we need to make the sum bigger by shifting our left pointer to the right
                l += 1
            # if threeSum == 0:
            else: 
                # add all 3 numbers to our result arr
                res.append([val, nums[l], nums[r]])
                # we only have to update one pointer because the other two above will be udpated there
                l += 1
                # if the current num value is equal to the previous value (and l < r because
                # we don't want our left pointer to pass the right pointer)
                while nums[l] == nums[l-1] and l < r:
                    # then we shift our left pointer to the right
                    l += 1

    return res

    ## time O(n log n) and O(n^2) #
    ## space O(n) --> because it takes up space to save it. it takes up memory. #


print(threeSum([-1, 0, 1, 2, -1, -4]))  #[[-1,-1,2],[-1,0,1]]
print(threeSum([0, 1, 1]))  # []
print(threeSum([0, 0, 0]))  # [[0,0,0]]