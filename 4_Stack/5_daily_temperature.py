'''
739. Daily Temperatures
Medium

Given an array of integers temperatures represents the daily temperatures, return 
an array answer such that answer[i] is the number of days you have to wait after 
the ith day to get a warmer temperature. If there is no future day for which this 
is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100'
'''

def dailyTemperatures(temperatures):
    ### O(n) solution using stacks ###
    stack = []
    output = [0] * len(temperatures)
    
    for i, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            j = stack.pop()
            output[j] = i - j
        stack.append(i)
        
    return output
    
    ### NeetCode solution O(n) time & memory using stacks ###
    ### Stack is always going ot be in monotonic decreasing order
    ### Add current_temp to stack. If the next day's temp is greater than current,
    ### pop current from stack and add 1 to output.
    ### If next day's temp is less than current, add next day temp to stack and
    ### do not update output. Continue.
    ### Once you get to a temp that is greater, you pop the current from the stack and
    ### update the corresponding position in the output. 
    ### Then you look at the previous of the current and update that position in output.
    
    # result = [0] * len(temperatures) # default values are automatically zeros
    # stack = [] # extra memory containing pairs of the temp and index to calculate difference (nums of days)
    
    # # Use enumerate to get the value and index at the same time
    # for i, temp in enumerate(temperatures):
    #     # Check to see if stack is empty and is temp greater than first item in our stack
    #     # In Python, the 1st item in stack is [-1] and the 1st temp is value of the pair [0]
    #     while stack and temp > stack[-1][0]:
    #         # If True, we're going to pop
    #         stackT, stackI = stack.pop()
    #         # For this temp, whatever its index was, we want to computer then umber of days 
    #         # it took to get warmer/greater temp by doing current temp we're at minus the 
    #         # index of the temp we just popped. We're adding the difference to the corresponding
    #         # position of the stack that we want.
    #         result[stackI] = (i - stackI)
    #     # Once the while loop is done executing, then we want to append pair to the stack.
    #     stack.append([temp, i])
    
    # return result 

    ### Attempting to solve using pointers / Brute force ### 
    ### The solution below is O(n^2) which is inefficient for larger inputs. ###
    ### When you run it in Leetcode, it says time limit exceeded. ###
    
    # result = []
    # i = 0
    
    # while i < len(temperatures):
    #     current_temp = temperatures[i]
    #     j = i + 1
    #     days_counter = 0
        
    #     while j < len(temperatures):
    #         if current_temp < temperatures[j]:
    #             days_counter = j - i
    #             result.append(days_counter)
    #             break
    #         j += 1
        
    #     if j == len(temperatures):
    #         result.append(0)
        
    #     i += 1
    
    # return result

print(dailyTemperatures([73,74,75,71,69,72,76,73])) #[1,1,4,2,1,1,0,0]
print(dailyTemperatures([30,40,50,60])) #[1,1,1,0]
print(dailyTemperatures([30,60, 90])) #[1,1,0]

print(dailyTemperatures([77,77,77,77,77,41,77,41,41,77])) #[0,0,0,0,0,1,0,2,1,0]
print(dailyTemperatures([55,38,53,81,61,93,97,32,43,78])) # [3,1,1,2,1,1,0,1,1,0]
print(dailyTemperatures([89,62,70,58,47,47,46,76,100,70])) # [8,1,5,4,3,2,1,1,0,0]