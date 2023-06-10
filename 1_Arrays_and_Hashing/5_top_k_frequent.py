'''Top K Frequent Elements

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
    ## First solution ##
    # d = {}
    # result = []
    
    # for num in set(nums):
    #     d[num] = 0

    # for n in nums:
    #     if n in d:
    #         d[n] += 1

    # # sort by value in descending order
    # d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))  

    # # while len(result) < k:
    # for key in d:
    #     result.append(key)
    #     if len(result) == k:
    #         break
        
    # return result

## time -> O(n log n)
## space -> O(m)

    ## Another solution with linear time and space O(n)##
    # bucket sort
    
    count = {} # hash map
    freq = [[]for i in range(len(nums) + 1)] # special arr -> same size as input arr
        ## index will be the freq or the count of elem, and value will be list of values that occurred that many particular number of times 
    
    ## iterate through every elem in nums
    for n in nums:
        count[n] = 1 + count.get(n, 0) # get count of how many times the elem occurred
    for n, c in count.items(): 
        freq[c].append(n) # c will be index, so we want to append n. So n occurs c number of times.
        
    res = []
    ## iterate through freq arr in descending order since we want to start with numbers that occur most frequently
    for i in range(len(freq)-1, 0, -1): # freq-1 means to the last index, and -1 means descending
        ## iterate trough every n value at freq[i]
        for n in freq[i]: # remember everything in i is another sublist
            res.append(n) # if it's not empty, we want to append n to our result because we want the value that occurs most frequently
            if len(res) == k: # when length of res reaches k, we want to stop
                return res
    




print(topKFrequent([1,1,1,2,2,3], k = 2))
print(topKFrequent([1], k = 1))
