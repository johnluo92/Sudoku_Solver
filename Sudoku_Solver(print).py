#!/usr/local/bin/python3
# find out how to populate each 0s with a random preset but unrepeated number in a square
# - find out what's already there
# - find out what's missing
# - randomly populate missing

# find out how to check each row/column/square combination for repeats

# def sudoku(puzzle):
#     """return the solved puzzle as a 2d array of 9 x 9"""

def try_number():
    global puzzle
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                for i in range(1,10):
                    if check_if_possible(row, col, i):
                        puzzle[row][col] = i
                        try_number() # 2. the return immediately after the check exits the step before
                        puzzle[row][col] = 0 # 3. the return cause this round of the loop to reset to 0
                return # 1. let's work backwards, if this is reached, retrace back one level

    print('final solution: ')
    print_puzzle()

def check_if_possible(row, col, num):
    global puzzle
    for i in range(9):
        if puzzle[row][i] == num:
            return False
        elif puzzle[i][col] == num:
            return False
        
    box_row = row // 3 *3 
    box_col = col // 3 *3
    
    for i in range(3):
        for j in range(3):
            if puzzle[box_row+i][box_col+j] ==num:
                return False
    return True


def print_puzzle():
    print()
    global puzzle
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print('- - - - - - - - - - - - -')
            
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print(' |  ', end='')

            if col == 8:
                print(puzzle[row][col])
            else:
                print(puzzle[row][col], end=' ')


puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

print_puzzle()
print('_____________________')
try_number()
# find_empty(puzzle)

