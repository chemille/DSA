'''22. Generate Parentheses
Medium

Given n pairs of parentheses, write a function to generate all combinations of 
well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
'''
        

def generateParenthesis(n):
    ## Neetcode's recursion and backtracking solution ##
    ## open (
    ## closed )
    ## If open count < n, add open
    ## If closed count < open count, add closed
    ## If closed count, open count, and n are all ==, then stop adding
    
    # stack = [] # holds our parentheses
    # res = [] # list of valid parens combo
    
    # def backtrack(open, closed):
    #     if open == closed == n:
    #         res.append("".join(stack)) # take every char in stack and join into string to append to res 
    #         return # then return because this is our base case
        
    #     if open < n:
    #         stack.append("(")
    #         print("open < n; +:", stack) #
    #         backtrack(open +1, closed) # recursively continue backtrack, increment open by 1, whenever we're done backtracking
    #         # pop the char we just added to the stack
    #         stack.pop()
    #         print("open < n; -:", stack) #
        
    #     if closed < open:
    #         stack.append(")")
    #         print("closed < open, +:", stack) #
    #         backtrack(open, closed +1)
    #         stack.pop()
    #         print("closed < open, -:", stack) #
            
    # backtrack(0, 0) # pass in 0 for initial open and closed count because stack is initially empty
    # return res
    
    
###### Another solution ####
    # res = [] # self.ans = []
    
    # def backtrack(curr, open, closed):
    #     ## Base case
    #     if open == closed == n:
    #         res.append(''.join(curr)) # self.ans.append("".join(curr))
    #         return
        
    #     if closed < open:
    #         curr.append(')')
    #         backtrack(curr, open, closed + 1)
    #         curr.pop()
            
    #     if open < n:
    #         curr.append('(')
    #         backtrack(curr, open + 1, closed)
    #         curr.pop()
        
    # backtrack(['('], 1, 0)
    # return res # return self.ans

    
##### Another solution #####
## The idea is to add ')' only after valid '('
## We use two integer variables open & closed to see how many '(' & ')' are in the current string
## If left < n then we can add '(' to the current string
## If right < left then we can add ')' to the current string

	def dfs(open, closed, s):
		if len(s) == n * 2: 
			res.append(s)
			return 

		if open < n:
			dfs(open + 1, closed, s + '(')

		if closed < open:
			dfs(open, closed + 1, s + ')')

	res = []
	dfs(0, 0, '')
	return res
        

print(generateParenthesis(3)) # ["((()))","(()())","(())()","()(())","()()()"]
print(generateParenthesis(1)) # ["()"]
