'''Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. Let these two numbers 
be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array 
[index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same 
element twice.

Your solution must use only constant O(1) extra space. 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. 
We return [1, 2].

Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. 
We return [1, 3].

Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. 
We return [1, 2].

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
'''
# enumerate with index starting 1 instead of 0
    # for i, num in enumerate(numbers):
        # if i not in dict:
            # dict[i] = num
# enumerate is O(1) time

def twoSum(numbers, target):  
    ####### Nested loop #########

    # res = []

    # for i in range(len(numbers) - 1):
    #     for j in range(i + 1, len(numbers)): 
    #         if numbers[i] + numbers[j] == target:
    #             res.append(i + 1)
    #             res.append(j + 1)
    #             return res  # Found the two indices

    # # If no solution found
    # return []

    ###### pointers ########

    left = 0 # left pointer starts at beginning of array
    right = len(numbers) - 1 # right pointer starts at end of array
    
    while left < right: # this ensures that once it meets in the middle, the loop will stop
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left + 1, right + 1]  # Found two indices accounting for starting at 1
        
        if current_sum < target:
            left += 1 
        else:
            right -= 1
    
    # # If no solution found
    return []



print(twoSum([2,7,11,15], 9)) # [1,2]
print(twoSum([2,3,4], 6)) # [1,3]
print(twoSum([-1, 0], -1)) # [1,2]
