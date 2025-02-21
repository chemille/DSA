'''
Search a 2D Matrix
Medium

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = 
[
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
], 
target = 3
Output: true

Example 2:
Input: matrix = 
[
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
], 
target = 13
Output: false
 
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
'''

def searchMatrix(matrix, target):
        ## My first solution ##
        ## This might be O(log(m*n)) ##
    
        # l_row = 0
        # r_row = len(matrix) - 1

        # for row in range(len(matrix)):
        #     m_row = l_row + (r_row - l_row) // 2
        #     for item in matrix[m_row]:
        #         if target == item:
        #             return True
        #         elif target > matrix[m_row][-1]:
        #             l_row = m_row + 1
        #         elif target < matrix[m_row][0]:
        #             r_row = m_row - 1

        # else:
        #     return False
   
    ## Copilot suggestions for binary search implementation ##
    ## Time complexity is O(log(m*n)), since m is the number of rows and n is the number of columns in the matrix
    ## This implementation uses a single binary search over the entire matrix, treating it as a flattened array, which ensures the time complexity is O(log(m * n)). ##
    
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = left + (right - left) // 2
        mid_value = matrix[mid // n][mid % n]

        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False
    
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)) # True
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)) # False
