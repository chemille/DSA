'''76. Minimum Window Substring
Hard

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in 
the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''

def minWindow(s, t) -> str:
    if s == t:
        return s
    
    if t == "" or len(t) > len(s):
        return ""
    
    # At minimum, the length of the output has to be the length of t

    # Create hashmaps for s and t to keep track of what's in window and t
    window = {}
    t_hash = {}
    
    for char in t:
        if char not in t_hash:
            t_hash[char] = 1
        # t_hash[char] = 1 + t_hash.get(char, 0)

    t_counter = 0
            
    # default values for result since we want the minimum
    result, result_len = [-1, -1], float("inf")       
    l = 0
    
    for r in range(len(s)):
        curr = s[r] 
        window[curr] = 1 + window.get(curr, 0)
        # If the current letter is in t_hash and the number of the letter in both hashes are the same
        if curr in t_hash and window[curr] == t_hash[curr]:
            t_counter += 1
        
        while t_counter == len(t):
            # update result
            # if the size of our window length (r - l + 1) is less than result_len
            if (r - l + 1) < result_len:
                result = [l, r]
                result_len = (r - l + 1)
            # pop from left of window to minimize
            window[s[l]] -= 1
            # If this char was in t_hash and if that char count in the window is less than in the t_hash
            if s[l] in t_hash and window[s[l]] < t_hash[s[l]]:
                t_counter -= 1 # decrememnt the counter since we removed from left of window
            l += 1 # remember to increment to left pointer to shift to the right since we're removing the left char
    
    # we can extract our left and right pointers to be the result        
    l, r = result
    
    if result_len != float("inf"):
        return s[l:r + 1]
    else:
        return ""
    # return s[l:r+1] if result_length != float("inf") else ""
    
## O(n) time

print(minWindow("ADOBECODEBANC", "ABC")) # "BANC"
print(minWindow("A", "A")) # "A"
print(minWindow("a", "aa")) # ""