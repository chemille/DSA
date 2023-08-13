'''424. Longest Repeating Character Replacement
Medium
9K
383
Companies
You are given a string s and an integer k. You can choose any character of the 
string and change it to any other uppercase English character. You can perform 
this operation at most k times.

Return the length of the longest substring containing the same letter you can get 
after performing the above operations.


Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
'''

def characterReplacement(s: str, k: int) -> int:
    # ## First solution ##
    # max_len_substring = 0
    # freq_map = {}
    # l = 0 # left pointer
    
    # for r in range(len(s)):  # r is the right pointer
    #     # for the char at position r, increment the count of it by doing 1 + current count. If char doesn't exist, it returns default 0. 
    #     freq_map[s[r]] = 1 + freq_map.get(s[r], 0) 

    #     # Make sure current window is valid. If the window length (r - l + 1) - most freq char
    #     # which gives number of replacements we have to do. And if this is > k:
    #     if (r - l + 1) - max(freq_map.values()) > k:
    #         freq_map[s[l]] -= 1 #take count of char at left position and decrement by 1
    #         l += 1 # shift left pointer to the right 
            
    #     # update max_len_substring
    #     max_len_substring = max(max_len_substring, r - l + 1) # size of window is r - l + 1
    # return max_len_substring

    # ## Time O(26*n) which is linear O(n) time
    
    ## NeetCode's second solution with slight optimization ## 
    count = {}
    res = 0
    l = 0
    maxf = 0 # max frequency in single variable 
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]]) # this is a constant time operation, not scanning anything
        
        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1
            
        res = max(res, r - l + 1)
    return res

print(characterReplacement("ABAB", 2)) # 4
print(characterReplacement("AABABBA", 1)) # 4
