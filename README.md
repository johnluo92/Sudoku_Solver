# Sudoku_Solver

link to the problem: https://www.codewars.com/kata/5296bc77afba8baa690002d7/python

Using backtracking algorithm and recursive function, this program is able to solve a 9x9 sudoku board

There are 3 solutions, two of them are very similar with slight variations in output, with the third one not being mine but its brevity caught my eye.

This mini-project is to strengthen my python skills and knowledge whilst completing online challenges such as the ones on hackerrank, codewars, and projecteuler.net.

The below is the recurisvely called function to repeatedly try a number in a cell given it's a validate move.

```python
def sudoku(puzzle):
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
                return puzzle # recursively return the result to the caller function
            puzzle[row][col] = 0
    return
```

In the printed version, the function reaches the last recursively called sudoku(puzzle) function and prints that puzzle, but it cannot return the result because it has implicitly returned None to the caller function.
