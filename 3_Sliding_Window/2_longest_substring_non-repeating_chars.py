'''3. Longest Substring Without Repeating Characters
Medium
36K
1.6K
Companies
Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

def lengthOfLongestSubstring(s: str) -> int:
    
    ## First solution ##
    # if len(s) <= 1:
    #     return len(s)

    # substring = s[0]
    # count = 0
    # for i in range(1, len(s)):
    #     if s[i] not in substring:
    #         substring += s[i]
    #     else:
    #         substring = substring[substring.index(s[i])+1:] + s[i]

    #     if len(substring) > count:
    #         count = len(substring)
    # return count

## NeetCode Solution ##
    # result variable initially set to 0
    res = 0
    # using set for substring -> memory complexity O(n)
    char_set = set()
    
    #sliding window with 2 pointers
    # left pointer starts at index 0
    l = 0
    
    # right pointer will continue to move 
    for r in range(len(s)):
        # if we find a duplicate, we need to update our window and char_set
        while s[r] in char_set: # if it's already in char_set, it's a duplicate
            char_set.remove(s[l]) # remove left most char and update left pointer
            l += 1
        char_set.add(s[r]) # add rightmost char to char_set
        # update result by taking the max between the current window and res
        res = max(res, r - l + 1) # current window size can be calculated by r-l+1 
    return res
        
            
print(lengthOfLongestSubstring("abcabcbb")) #3
print(lengthOfLongestSubstring("bbbbbb")) #1
print(lengthOfLongestSubstring("pwwkew")) #3
print(lengthOfLongestSubstring("dvdf")) #3
print(lengthOfLongestSubstring("anviaj")) #5