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

    # Approach # 2 # hash map # 

    hash = {}
    if len(s) != len(t):
        return False

    for letter in s:
        if letter not in hash:
            hash[letter] = 1
        else:
            hash[letter] += 1

    for letter in t:
        if letter in hash:
            hash[letter] -= 1

    for val in hash.values():
        if val > 0:
            return False

    return True

print(is_anagram("rat","car")) # false
print(is_anagram("sort","tors")) # true
print(is_anagram("anagram", "nagaram")) # true
