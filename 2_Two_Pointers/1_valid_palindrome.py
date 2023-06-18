'''Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 
Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''
# Pseudocode: 
# Create a new empty string.
# Convert the string to lowercase, remove symbols.
# use negative slicing to check if is == to the converted string.
# Return true or false

def isPalindrome(word):
    
    new_string = ""

    for letter in word:
        if letter.isalnum():
            new_string += letter.lower()
    
    return new_string == new_string[::-1]


print(isPalindrome( "A man, a plan, a canal: Panama"))#true
print(isPalindrome("race a car"))#False
print(isPalindrome(" "))#True


