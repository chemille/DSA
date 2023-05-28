from collections import Counter
'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
'''

def is_anagram(s,t):
    # Approach # 1 # sorted#
    # if sorted(s) == sorted(t):
        # return True
    # return False
    
    ## Same as above, but just a one liner
    return sorted(s) == sorted(t)
    ## time for sorting is O(n log n) and space is O(1) because it didn't take up extra space

    # Approach # 2 # hash map # 
    # hash = {}

    # if len(s) != len(t):
    #     return False

    # for letter in s:
    #     if letter not in hash:
    #         hash[letter] = 1
    #     else:
    #         hash[letter] += 1

    # for letter in t:
    #     if letter in hash:
    #         hash[letter] -= 1

    # for val in hash.values():
    #     if val > 0:
    #         return False

    # return True

    # Approach # 3 # hash map and using count method
    # if len(s) != len(t):
    #     return False
    
    # countS, countT =  {}, {}
    
    # for i in range(len(s)):
    #     # building the hashmaps 
    #     countS[s[i]] = 1 + countS.get(s[i], 0) # 0 is a default value
    #     countT[t[i]] = 1 + countT.get(t[i], 0) 
    # for key in countS:
    #     if countS[key] != countT.get(key, 0): # get is used in case countT does not have the key that countS does have. 
    #         return False
    # return True

    ## time and space would be O(s+t) because we have to iterate through both strings
    ## and create hashmaps that are potentially up to the size of s + t.

    # Approach # 4 # Counter method
    # Counter is a data structure in Python which is a hashmap, but counts thing automatically for you.
    # Basically does the same thing as previous solution, but in one line of code.
    return Counter(s) == Counter(t)
    
    
print(is_anagram("rat","car")) # false
print(is_anagram("sort","tors")) # true
print(is_anagram("anagram", "nagaram")) # true
