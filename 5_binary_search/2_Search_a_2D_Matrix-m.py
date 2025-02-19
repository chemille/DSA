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
        ## Time complexity should be O(m*n), since m is the number of rows and n is the number of columns in the matrix
        ## Basically visiting each element of the matrix once
    
        l_row = 0
        r_row = len(matrix) - 1

        for row in range(len(matrix)):
            m_row = l_row + (r_row - l_row) // 2
            for item in matrix[m_row]:
                if target == item:
                    return True
                elif target > matrix[m_row][-1]:
                    l_row = m_row + 1
                elif target < matrix[m_row][0]:
                    r_row = m_row - 1

        else:
            return False
   

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)) # True
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)) # False
