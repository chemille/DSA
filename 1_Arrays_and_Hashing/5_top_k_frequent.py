'''Top K Frequent 

Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
uim,
Input: nums = [1], k = 1
Output: [1]

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''

def topKFrequent(nums, k):

    d = {}
    result = []
    
    for num in set(nums):
        d[num] = 0

    for n in nums:
        if n in d:
            d[n] += 1

    # sort by value in descending order
    d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))  

    # while len(result) < k:
    for key in d:
        result.append(key)
        if len(result) == k:
            break
        
    return result

## time -> O(n log n)
## space -> O(m)

# Step 1: Count the frequency of each element
#     freq = {}
#     for num in nums:
#         if num in freq:
#             freq[num] += 1
#         else:
#             freq[num] = 1
    
#     # Step 2: Sort the elements based on frequency in descending order
#     sorted_nums = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
#     print(sorted_nums)
    
#     # Step 3: Extract the k most frequent elements
#     result = sorted_nums[:k]
    
#     return result


print(topKFrequent([1,1,1,2,2,3], k = 2))
print(topKFrequent([1], k = 1))
