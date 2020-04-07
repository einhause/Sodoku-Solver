#
#
#   @author: Eric Einhaus
#
#


from sodokuSolver import SodokuSolver

#Some puzzles to solve from, copy and paste to the input the program asks for

easyPuzzles = ['sudokus/s01a.txt', 'sudokus/s01b.txt', 'sudokus/s01c.txt',
                'sudokus/s02a.txt', 'sudokus/s02b.txt', 'sudokus/s02c.txt',
                'sudokus/s06a.txt', 'sudokus/s06b.txt', 'sudokus/s06c.txt',
                'sudokus/s10a.txt', 'sudokus/s10b.txt', 'sudokus/s10c.txt',
                'sudokus/s13a.txt', 'sudokus/s13b.txt', 'sudokus/s13c.txt',]

medPuzzles = ['sudokus/s03a.txt', 'sudokus/s03b.txt', 'sudokus/s03c.txt',
                'sudokus/s04a.txt', 'sudokus/s04b.txt', 'sudokus/s04c.txt',
                'sudokus/s07a.txt', 'sudokus/s07b.txt', 'sudokus/s07c.txt',
                'sudokus/s11a.txt', 'sudokus/s11b.txt', 'sudokus/s11c.txt',
                'sudokus/s14a.txt', 'sudokus/s14b.txt', 'sudokus/s14c.txt',]

hardPuzzles = ['sudokus/s05a.txt', 'sudokus/s05b.txt', 'sudokus/s05c.txt',
                'sudokus/s08a.txt', 'sudokus/s08b.txt', 'sudokus/s08c.txt',
                'sudokus/s09a.txt', 'sudokus/s09b.txt', 'sudokus/s09c.txt',
                'sudokus/s12a.txt', 'sudokus/s12b.txt', 'sudokus/s12c.txt',
                'sudokus/s15a.txt', 'sudokus/s15b.txt', 'sudokus/s15c.txt', 'sodokus/s16.txt']

unsolvablePuzzles = ['sudokus/unsolvable.txt', 'sudokus/unsolvable2.txt', 'sudokus/unsolvable3.txt']


class TestSodukuSolver:
    if __name__ == "__main__":
        print('Please provide the name of the text file containing the sudoku puzzle to solve:')
        file = input() 
        solver = SodokuSolver(file)
        solver.print_starting_board(solver.board)
        solver.print_solved_board(solver.board)
