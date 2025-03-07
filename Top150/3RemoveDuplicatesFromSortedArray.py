'''
Remove Duplicates from Sorted Array
Easy

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:
1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
'''

def removeDuplicates(nums) -> int:        
    # Modify sorted array in place
    # Pointers: one to iterate through array starting at index 1, and 
    # second pointer (curr / k) to track the position of the next valid element.
    # Set k pointer at 1.
    # Initialize count variable to track how many times the curr / k elem has been encountered.
    # Compare nums[i] to nums[i-1]
        # If they're not equal:
            # Reset count to 0.
            # Replace with valid elem at position k --> nums[k] = nums[i]
            # shift k to right
        # Otherwise, if they are equal:
            # count += 1
            # Once the count gets to 2+, we don't want the position of k moving yet.
            # We want k to stay until we get to a new nums[i] to replace with.
            # If count is less than 2,
                # replace with valid elem --> nums[k] = nums[i]
                # shift k to right
    
    ## O(n) time, O(1) space solution ##

    k = 1
    count = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            count = 0
            nums[k] = nums[i]
            k += 1
        else: 
            count += 1 
            if count < 2: 
                nums[k] = nums[i]
                k += 1
    return k

print(removeDuplicates([1,1,1,2,2,3])) # Output: 5, nums = [1,1,2,2,3]
print(removeDuplicates([0,0,1,1,1,2,2,3,3])) # Output: 7, nums = [0,0,1,1,2,2,3]
print(removeDuplicates([1,1,2])) # Output 3, nums = [1,1,2]

