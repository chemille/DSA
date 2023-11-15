'''GROUP ANAGRAMS
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.'''

def group_anagrams(strs) -> list:
    ## First solution
    # sorted_words = {}

    # for word in strs:
    #     word_key = ''.join(sorted(word))
    #     if word_key not in sorted_words:
    #         sorted_words[word_key] = []
    #     if word_key in sorted_words:
    #         sorted_words[word_key].append(word) # append the word as a value 
        
    # return list(sorted_words.values())

# Time complexity -> O(n * k * log(k)), where N is the number of words in the strs list and K is the maximum length of a word in strs.
    # Sorted fx takes O(n long n) time
    # Adding items to a dict takes O(1) time on average
    # Converting sorted_words.values() to a list takes O(n) time
    
# Space complexity -> O(n * k), where N is the number of words in strs and K is the maximum length of a word in strs. This is because the sorted_words dictionary can store at most N entries, and each entry can have a word of length K.

# Overall, the time complexity is O(N * K * log(K)) aka polynomial time complexity, and the space complexity is O(n * k).

    ## Another solution 
        strs_dict = {}

        for word in strs:
            sorted_word = sorted(word)
            joined_word = "".join(sorted_word)

            if joined_word in strs_dict:
                strs_dict[joined_word].append(word)
            else: 
                strs_dict[joined_word] = [word]

        return [strs_dict[key] for key in strs_dict]

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
print(group_anagrams([""]))
print(group_anagrams(["a"]))
