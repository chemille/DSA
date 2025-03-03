'''
Merge Sorted Array
Easy

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 
Constraints:
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
'''

# Merge in reverse order, starting from the largest values 
# Use pointer that starts at the last position in nums1
    # p = (m + n) - 1 OR len(nums) - 1
# Also use m and n as pointers to keep track of positions in each array
# We want to loop while there are element still left in both arrays
    # while m > 0 and n > 0:
# Compare largest values, so nums1[m-1] and nums2[n-1]
    # nums1 = [1,2,3,0,0,0] and nums2=[2,5,6]
                #  ^m    ^p                ^n
# In this case, nums2[n-1] > nums1[m-1] # 6 > 3
# So we want to replace the 0 at the p position with 6
    # nums1[p] = nums2[n - 1]
# Update pointers: m stays, n -= 1, p -= 1
# Now nums1 = [1,2,3,0,0,6] and nums2=[2,5,6]
                #  ^m  ^p               ^n
# Compare: nums2[n - 1] > nums1[m - 1] # 5 > 3
# So we want to replace the 0 at the p position with 5
    # nums1[p] = nums2[n - 1]
# Update pointers: m stays, n -= 1, p -= 1
# Now nums1 = [1,2,3,0,5,6] and nums2=[2,5,6]
                #  ^m^p                ^n
# Compare: nums2[n - 1] <= nums1[m - 1]  # 2 <= 3
# This time, we're going to replace 0 with the value to the left of it
    # nums1[p] = nums1[m - 1]
# Update pointers:  m -= 1, p -= 1, n stays
# Now nums1 = [1,2,0,3,5,6] and nums2=[2,5,6]
            #    ^m^p                  ^n
# Compare: nums2[n-1] <= nums1[m-1] # 2 <= 2
    # nums1[p] = nums1[m-1]
# Update pointers: m -= 1, p -= 1, n stays
# Now nums1 = [1,2,2,3,5,6] and nums2=[2,5,6]
            #  ^m^p                    ^n
# Now it will exit the while loop 

# In the cases where there are smaller numbers that need to be added to the left of nums1
# For example, nums1 = [0,2,2,3,5,6] and nums2 = [1,5,6]
                    #   ^m^p                      ^n
# We need another while loop for this so that it will add all the smaller numbers from nums2 into nums1 one by one
    # while n > 0:
        # nums1[p] = nums2[n - 1]
# Update pointers: m stays, n -= 1, p -= 1

def merge(nums1, m, nums2, n) -> None:
    p = len(nums1) - 1
    
    while m > 0 and n > 0:
        if nums2[n  - 1] > nums1[m - 1]:
            nums1[p] = nums2[n - 1]
            n -= 1
        else: # nums2[n - 1] <= nums1[m - 1]
            nums1[p] = nums1[m - 1]
            m -= 1
        p -= 1

    while n > 0:
        nums1[p] = nums2[n - 1]
        n -= 1
        p -= 1

    ## Neetcode solution O(n+m), O(1) ##
        # # Get last index of nums1
        # last = m + n - 1
        # # Merging in reverse order while there are elements left in both arrays
        # while m > 0 and n > 0:
        #     # Get largest value in each array to compare
        #     # If the largest number in nums1 is greater than the last number in nums2, replace that last 0 of nums1 with nums2[n]
        #     if nums1[m - 1] > nums2[n - 1]:
        #         nums1[last] = nums1[m - 1]
        #         # Update pointer
        #         m -= 1
        #     else: # Else if nums1[m] <= nums2[m]
        #         nums1[last] = nums2[n - 1]
        #         n -= 1
        #     # Regardless of which number we insert, we want to decrement last index of nums1
        #     last -= 1

        # # Fill nums1 with the leftover elements in nums2 
        # while n > 0:
        #     nums1[last] = nums2[n - 1]
        #     # Update pointers
        #     n -= 1
        #     last -= 1

print(merge([1,2,3,0,0,0], 3, [2,5,6], 3)) #Output: [1,2,2,3,5,6]
print(merge([1], 1, [], 0)) # Ouput: [1]
print(merge([0], 0, [1], 1)) # Ouput: [1]

## Solutions pass on Leetcode!
