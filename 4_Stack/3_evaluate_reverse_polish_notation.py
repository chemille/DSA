'''
150. Evaluate Reverse Polish Notation
Medium

You are given an array of strings tokens that represents an arithmetic expression in a 
Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
'''

def evalRPN(tokens) -> int:
    
    # stack = []
    # for item in tokens:
    #     if item == '+':
    #         stack.append(stack.pop() + stack.pop())
    #     elif item == '*':
    #         stack.append(stack.pop() * stack.pop())
    #     elif item =='-':
    #         first, second = stack.pop(), stack.pop()
    #         stack.append(second - first)
    #     elif item =='/':
    #         first, second = stack.pop(), stack.pop()
    #         stack.append(int(second / first))
    #     else:
    #         stack.append(int(item))
    # return stack[0]

    ## Time O(n) because going through input string, adding and removing at once each.
    ## Space O(n) because we use a stack. 
    
##### Another solution ###
    # while len(tokens) > 1:
    #     t = tokens.pop(0)
    #     if t not in '+-*/': 
    #         tokens.append(t)
    #     else:
    #         num1, num2 = tokens.pop(), tokens.pop()
    #         tokens.append(str(int(eval(''.join([num2,t,num1])))))
    # return int(tokens[0])
    
    
##### Another solution ####
    stack = []
    for char in tokens:
        if char not in '+-*/':
            stack.append(char)
        else:
            num1, num2, = stack.pop(), stack.pop()
            new_num = str(int(eval(''.join([num2, char, num1]))))
            stack.append(new_num)
    return int(stack[0])    

## Time -> operation of pushing onto a stack takes O(1) constant time, and the eval function
## could be considered constant time for basic arithmetic operations, but it's not a constant-time
## operation in general due to parsing and evaluation involved. Since each item is processed
## once and each operation wihtin the loop can be considered constant time (ignoring the 'eval'
## complexities) so the overall time complexity is approximated as O(n) linear, where n is 
# the number of items in the input.
## Space -> determined by the stack that holds operands during the evaluation. Worst case, the 
## stack might hold all the operands from the input list before they are gradually popped. 
## Therefore, space is O(n) linear, where n is the number of items in the input.

print(evalRPN(["2","1","+","3","*"])) #9
print(evalRPN(["4","13","5","/","+"])) #6
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])) #22

