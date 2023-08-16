'''567. Permutation in String
Medium

Given two strings s1 and s2, return true if s2 contains a permutation of s1, 
or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''
from itertools import permutations

def checkInclusion(s1, s2):
    ## My solution works for short inputs, but for longer inputs it exceeds the memory limit ##
    # if len(s1) > len(s2):
    #     return False
    
    # if s1 in s2:
    #     return True
    # # using itertools to get list of permutations of s1
    # words = [''.join(char) for char in permutations(s1)]
    
    # for word in words: 
    #     if word in s2:
    #         return True
    # else:
    #     return False
    
    ## NeetCode's O(n) Solution ##
    ## Sliding window technique.
    ## Create hashmap or array for s1 and another for s2.
    ## Initialize variable for matches, which will maintain the total number of 
    ## equal chars between each of the hashmaps. If there is a match, it gets +1.
    # It could be 26 matches or less.
    
    if len(s1) > len(s2):
        return False
    
    # Initialize each array to have 0s for now
    s1_count, s2_count = [0] * 26, [0] * 26
    
    # Iterate through every char in s1 
    for i in range(len(s1)):
        # Get char at ith index of s1_count and use the ord function to get the ascii value of that char
        # Subtract the ascii of lowercase 'a' and increment by 1. This will map to the indices.
        s1_count[ord(s1[i]) - ord('a')] += 1
        # Do the same for s2_count
        s2_count[ord(s2[i]) - ord('a')] += 1
    
    # Initialize number of matches to 0
    matches = 0
    # Compare each of arrays
    for i in range(26):
        # To the number of matches, we want to add 1 to it only if s1_count's index is equal to s2_count's index i
        if s1_count[i] == s2_count[i]:
            matches += 1
        # else we do nothing
    
    # Sliding window
    l = 0 # left pointer 
    # r is the right pointer. Start range at len of s1 because that will start us off at the char we left off at.
    #       
    for r in range(len(s1), len(s2)):
        if matches == 26:
            return True
        # map char to index to get index of our count array
        index = ord(s2[r]) - ord('a')
        # this is the char that just got added to our window in our s2 string, so we're incrementing by 1.
        s2_count[index] += 1
        # now that incremented this, if it equals the char at s1, then increment matches 
        if s1_count[index] == s2_count[index]:
            matches += 1
        elif s1_count[index] + 1 == s2_count[index]:  
            matches -= 1
        # With index r, we're adding a char to the right. But at index l, we're removing a char.
        # So we do the decrement the count from the left side of our window.
        index = ord(s2[l]) - ord('a')
        s2_count[index] -= 1
        if s1_count[index] == s2_count[index]:
            matches += 1
        elif s1_count[index] - 1 == s2_count[index]:  
            matches -= 1
        # Remember to increment left pointer
        l += 1
    # If matches == 26, it will return True. Else False. 
    return matches == 26
        
        
print(checkInclusion("ab", "eidboaoo")) # false
print(checkInclusion("ab", "eidbao0o")) # true
print(checkInclusion("dinitrophenylhydrazine", "acetylphenylhydrazine")) # false
print(checkInclusion("trinitrophenylmethylnitramine", "dinitrophenylhydrazinetrinitrophenylmethylnitramine")) # true
