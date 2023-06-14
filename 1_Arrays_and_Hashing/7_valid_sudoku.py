''' Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false

Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
'''

import collections

def sudoku(board):
    # Initialize rows to create a list of sets. It initializes each set as an empty set 
    # using the set() constructor. The list comprehension [set() for _ in range(9)] iterates 
    # over the range from 0 to 8 (9 iterations) using the placeholder variable _. 
    # On each iteration, it creates a new empty set and adds it to the list.
    rows = [set() for _ in range(9)]
    columns = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)] 
    # In the context of the list comprehension [set() for _ in range(9)], the underscore _ is 
    # often used as a convention to represent a variable that is not going to be used/accessed 
    # within the loop. Typically used as a placeholder when the actual value of the iterator 
    # is not needed.

    for r in range(9):
        for c in range(9):
            digit = board[r][c]
            if digit != ".":
                if digit in rows[r] or digit in columns[c] or digit in boxes[(r // 3) * 3 + (c // 3)]:
                    return False
                rows[r].add(digit)
                columns[c].add(digit)
                boxes[(r // 3) * 3 + (c // 3)].add(digit)

    return True

    ## NeetCode solution ##
    # cols = collections.defaultdict(set)
    # rows = collections.defaultdict(set)
    # squares = collections.defaultdict(set) # key = (row //3, col // 3)

    # for r in range(9):
    #     for c in range(9):
    #     if board[r][c] == ".":
    #         continue
    #     if(board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]):
    #         return False
    #     cols[c].add(board[r][c])
    #     rows[r].add(board[r][c])
    #     squares[(r//3, c//3)].add(board[r][c])
    # return True

print(sudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
# true
print(sudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
# false