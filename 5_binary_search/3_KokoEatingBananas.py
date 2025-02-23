'''Koko Eating Bananas
You are given an integer array piles where piles[i] is the number of bananas in the ith pile. 
You are also given an integer h, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, you may finish eating the pile but you cannot eat from another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h hours.

Example 1:
Input: piles = [1,4,3,2], h = 9
Output: 2
Explanation: With an eating rate of 2, you can eat the bananas in 6 hours. 
With an eating rate of 1, you would need 10 hours to eat all the bananas (which exceeds h=9), thus the minimum eating rate is 2.

Example 2:
Input: piles = [25,10,23,4], h = 4
Output: 25

Constraints:
1 <= piles.length <= 1,000
piles.length <= h <= 1,000,000
1 <= piles[i] <= 1,000,000,000

Recommended Time & Space Complexity
You should aim for a solution with O(nlogm) time and O(1) space, 
where n is the size of the input array, and m is the maximum value in the array.
'''

import math

def minEatingSpeed(piles, h):
    ## Try brute force solution first ##
    ## Thinking nested loops which would be time O(m*n)
    ## Initialize minimum eating speed to 1
    ## Iterating through all possible eating speed range from 1 to max(piles) 
        ## Initialize hours variable to track total hours taken to eat for each eatingSpeed
        ## Iterate through each pile in piles to calculate hours
            ## hours += math.ceil(each pile / eating speed) <-- rounds down
        ## If hours is less than or equal to h
            ## return the eating speed
        ## Increment eating speed by 1
    ## return eating speed

    # eatingSpeed = 1 

    # for i in range(1, max(piles)): 
    #     hours = 0 
    #     for p in piles: 
    #         hours += math.ceil(p / eatingSpeed) 
    #     if hours <= h:
    #         return eatingSpeed
    #     eatingSpeed += 1

    # return eatingSpeed

    ## Binary search solution with Neetcode ##
    ## Time O(n * log m), Space O(1) ##

    # low = 1 
    # high = max(piles) 
    # output = high # this is the max that will work worst case scenario

    # while low <= high:
    #     mid = (high + low) // 2
    #     hours = 0
    #     for p in piles:
    #         hours += math.ceil(p / mid) ## Rounds up
    #     if hours <= h:
    #         output = min(mid, output)
    #         high = mid - 1
    #     else: 
    #         low = mid + 1
        
    # return output

    ## Another solution with binary search not importing math ##
    l, r = 1, max(piles)
    
    while l <= r:
        mid = (l + r) // 2
        ## Uses list comprehension to calculate the total number of hours Koko needs to eat all the bananas at a given eating speed mid.
        total_hours = sum((pile + mid - 1) // mid for pile in piles)
        ## pile + mid - 1 ensures that the division rounds up, which is equivalent to math.ceil(pile / mid).
        ## The list comprehension iterates over each pile in piles and calculates the number of hours needed to eat that pile at the current eating speed mid.
        ## sum(...) adds up the hours for all piles to get the total number of hours needed.
        ## This total is then used to determine if the current eating speed mid allows Koko to eat all the bananas within the given hours h.            
        if total_hours > h:
            l = mid + 1
        else:
            r = mid - 1
            
    return l

assert minEatingSpeed([3,6,7,11], 8) == 4
assert minEatingSpeed([30,11,23,4,20], 5) == 30
assert minEatingSpeed([30,11,23,4,20], 6) == 23 
print("All test cases passed!")
