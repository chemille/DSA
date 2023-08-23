'''20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

# Stack -> LIFO
# Iterate through string
# If it's open '(', '{', or '[', append to stack.
# If the next iteration is a matching closing bracket, pop from stack. 
# Otherwise, return False

def isValid(s) -> bool:

    ### One Solution ##
    # open_symbols = []

    # for c in s:
    #     if c in ['(', '{', '[']:
    #         open_symbols.append(c)
    #     elif c == ')' and len(open_symbols) != 0 and open_symbols[-1] == '(':
    #         open_symbols.pop()
    #     elif c == '}' and len(open_symbols) != 0 and open_symbols[-1] == '{':
    #         open_symbols.pop()
    #     elif c == ']' and len(open_symbols) != 0 and open_symbols[-1] == '[':
    #         open_symbols.pop()
    #     else:
    #         return False
    # return open_symbols == []


    ### NeetCode solution ##
    ### Using stack and dict, where closing symbol is key and opening symbol is the value ##
        stack = []
        close_to_open = {
            ")": "(", 
            "]": "[", 
            "}": "{" 
        }
        
        for c in s:
            if c in close_to_open:
                # If the stack has data and the last item is the matching value
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
                
        return True if not stack else False
    
print(isValid("()")) # true
print(isValid("()[]{}")) # true
print(isValid("(]")) # false
print(isValid("([)]")) # false



