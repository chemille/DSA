''' Encode and Decode Strings 
This problem is only available on leetcode premium, so go to this link to access 
-> lintcode.com/problem/659/

Description: Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Example1

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
Example2

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"

'''

"""
@param: strs: a list of strings
@return: encodes a list of strings to a single string.
"""
def encode(strs):
    start_str = ''
    separator = ';'
    i = 0
    for i, word in enumerate(strs):
        if i > 0:
            start_str += separator
        start_str += str(len(word)) + separator + word 

    return start_str

"""
@param: str: A string
@return: decodes a single string to a list of strings
"""
def decode(str):

    start_str = encode(str)
    str_store = []
    separator = ';'

    substring = '' 
    i = 0
    for i, char in enumerate(start_str):
        if char != separator and char.isnumeric() == False:
            substring += char
        # if char == separator and start_str[i-1].isalpha():
        if char == separator and start_str[i-1].isnumeric() == False:
            str_store.append(substring)
            substring=''
    str_store.append(substring)  

    return str_store  

############ NeetCode Solution O(n) #################
# def encode(strs):
#     res = ''
#     for s in strs:
#         res += str(len(s)) + '#' + s

#     return res

# def decode(str):
#     res, i  = [], 0 # pointer i will tell us what position we're at in the string

#     while i < len(str): # each iteration reads one entire word until we reach the end 
#         j = i
#         while str[j] != '#':
#             j += 1
#         length = int(str[i:j])
#         res.append(str[j + 1: j + 1 + length]) # j + 1 + length will give us the entire string
#         i = j + 1 + length
#     return res

print(encode(["lint","code","love","you"]))
print(encode(["we", "say", ":", "yes"]))
print(decode(["lint","code","love","you"]))
print(decode(["we", "say", ":", "yes"]))