from collections import defaultdict

'''CONTAINS DUPLICATE
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true'''

def is_duplicate(nums):
    # Approach # 1 # hashmap

    # d = {}

    # for num in nums:
    #   if num in d:
    #     d[num] +=1
    #   else:
    #     d[num] = 1

    # for value in d.values():
    #  if value > 1:
    #    return True
    # return False

    # Approach # 2 # sets
    # set_nums = set(nums)

    # if len(set_nums) != len(nums):
    #   return True

    # return False

    #Approach # 3 #sorted way

    # numss = sorted(nums)
    # print("numms is",numss)

    # for i in range(len(numss)-1):
    #   i = 0
    #   j = i+1
    #   # print(i,j)
    #   if numss[i] == numss[j]:
    #     return True
    #     j +=1
    #   else:
    #     return False
    
    
    # Approach # 4 # brute force

    # for i in range(len(nums) - 1):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] == nums[j]:
    #                 return True

    # return False

    # Approach # 5 # counter class
    counter = defaultdict(int)

    for n in nums:
        counter[n] += 1

    for val in counter.values():
        if val > 1:
            return True
    return False
    


print(is_duplicate([1,2,3,1])) # true
print(is_duplicate([1,2,3,4])) # false
print(is_duplicate([1,1,1,3,3,4,3,2,4,2])) # true