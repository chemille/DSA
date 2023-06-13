
'''Product of Array Except Self
Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''
# We want to multiply every value in nums EXCEPT for the current num itself.
# For example, if we want the product here of every num [1,2,3,4] except for 3, then
# we can break it down by getting the product of the nums before 3 and after 3, and then
# multiply these two values together which would give us the value we want for this example.
# So we can get the prefix values by multiplying the first iteration to the second.
#     Next, multiply the secodn to the third iteration. Then, the third to the fourth.
#     nums = [1,2,3,4] 
#     -> 1 -> 1x2 -> 2x3 -> 6x4 
#     prefix -> [1,2,6,24] 
# We can also get postfix by doing the exact same thing in reverse order.   
#     nums = [1,2,3,4] 
#      24x1 <- 12x2 <- 4x3 <- 4
#     postfix -> [24, 24, 12, 4]
# For the ouput, we want to treat as if the prefix before the first num and postfix after last num is 1.
# We want the prefix value the comes before the current and postfix value that comes after current.
# output -> 1x24 -> 1x12 -> 2x4 -> 6x1 -> [24, 12, 8, 6]
# This would be an O(n) solution for T + S. But if we don't create the prefix and postfix tables,
# it would be O(n) time and O(1) space.

def productExceptSelf(nums):
    # create result output array with an initial value of 1 * len of input arr   
    result = [1] * len(nums)
    # initialize prefix as 1 and iterate through each position in arr
    prefix = 1
    for i in range(len(nums)):
        # put value in that position i
        result[i] = prefix
        # take input arr's val * val of prefix
        prefix *= nums[i]
        # prefix gets stored in input arr

    postfix = 1
    # for postfix, we start at the end of the input arr and go up until the beginning
    for i in range(len(nums) - 1, -1, -1): 
        # with postfix, we're going to multiply to val already in results (which is the prefix)
        result[i] *= postfix
        # continue to update postfix by multiplying to the val that is in the input arr nums
        postfix *= nums[i]

    return result

print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))