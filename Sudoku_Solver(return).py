#!/usr/local/bin/python3
# find out which cell is 0 and how to populate them
# recursively do the following:
# - find out what's already there
# - find out what's missing
## for Code_wars
    
def sudoku(puzzle):
    
    # used to find an empty cell
    def find_empty_cell(puzzle):
        for row in range(9):
            for col in range(9):
                if puzzle[row][col] == 0:
                    return row,col
        return

    found_empty = find_empty_cell(puzzle)
    
    # base case if no cell is empty (when last cell is populated)
    if not found_empty:
        return puzzle
    # recursive state: found empty cell
    else:
        row, col = found_empty
    for i in range(1,10):
        if check_if_possible(row, col, i):
            puzzle[row][col] = i

            if sudoku(puzzle):
                return puzzle #returning true will not cause cell to be assigned 0
            puzzle[row][col] = 0 # assigned 0 only when all values failed to satisfy
    return # if this is reached, retrace back one level and assign that cell 0
    
def check_if_possible(row, col, num):
    global puzzle
    for i in range(9):
        if puzzle[row][i] == num:
            return
        elif puzzle[i][col] == num:
            return
        
    box_row = row // 3 *3 
    box_col = col // 3 *3
    
    for i in range(3):
        for j in range(3):
            if puzzle[box_row+i][box_col+j] ==num:
                return
    return True


def print_puzzle(puzzle):
    print()
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

print_puzzle(puzzle)
print('_________________________')
sudoku(puzzle)
print_puzzle(puzzle)
