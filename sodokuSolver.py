#
#
#   @author: Eric Einhaus
#
#


class SodokuSolver:
    board = [[]]
    
    
    def __init__(self, file):
        
        __slots__ = [ "_file" ]
        
        self._file = file
        self.board = self.parse_board(self._file)       
        

    #Parses the text files of strings of numbers, resembling a 9x9 sudoku grid
    def parse_board(self, fileName):
        newBoard = list(list())
        with open(fileName) as f:
            for line in f:
                for i in range(9):
                    newRow = line.split(' ')
                    newBoard.append(newRow)
                    line = f.readline()
        return newBoard
            
    #Prints the broad with borders for a organized graphical interface on the module
    def print_board(self, puzz):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("---------------------")
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("| ", end="")

                if j == 8:
                    print(str(puzz[i][j]))
                else:
                    print(str(puzz[i][j]) + " ", end="")

    #Prints the initial board (not solved) with 0's representing empty spaces
    def print_starting_board(self, puzz):
        print("\n----------------\nStarting Board: \n----------------\n")
        self.print_board(puzz)

    #Solved the board and prints the results. If the puzzle is unsolvable, an error is thrown
    def print_solved_board(self, puzz):
        if self.sodoku_solver(puzz):
            print("\n----------------\nSolved Board: \n----------------\n")
            self.print_board(puzz)
        else:
            raise ValueError("\n\n----------------------------\nERROR: Board is not Solvable! \n----------------------------\n")

    #finds the next empty space on the sodoku board
    def an_empty_space(self, puzz):
        for i in range(9):
            for j in range(9):
                if puzz[i][j] == str(0):
                    return (i, j)
        return None

    #returns a boolean value checking if the number placed on the board is satsfiable
    #by the row, column, and box that its in. if a constraint occurs in the row, column,
    #or box, return False. Otherwise, return True
    def valid_num(self, puzz, coordinate, num): #data types: self, [][], tuple(), str
        # 1) Check to see if the row is satisfied
        for i in range(9): 
            if puzz[coordinate[0]][i] == str(num) and coordinate[1] != i:
                return False
        # 2) Check to see if the column is satisfied
        for j in range(9): 
            if puzz[j][coordinate[1]] == str(num) and coordinate[0] != j:
                return False
        # 3) Check to see if the box is satisfied
        x = (coordinate[0] // 3) * 3
        y = (coordinate[1] // 3) * 3
        

        for i in range(3):
            for j in range(3):
                if puzz[x+i][y+j] == str(num) and (x+i, y+j) != coordinate:
                    return False
                  
        return True



    #the main algorithm, finds an empty space (if None, the algorithm is complete). Tries
    #the range of numbers from 1 to 9, checks to see if the number is satisfiable, and
    #adds it to the board if True. This is done recursively. checking for backtracking, and
    #returns True once there are no empty spaces remaining and no constraints remain
    def sodoku_solver(self, board):
        
        anEmptySpace = self.an_empty_space(board)

        if anEmptySpace == None:
            return True

        x = anEmptySpace[0]
        y = anEmptySpace[1]
        
        for i in range(1, 10):
            if self.valid_num(board, anEmptySpace, i):
                board[x][y] = str(i)
                
                #the recursive call, only returns true if the board is satisfied and no empty spaces remain
                if self.sodoku_solver(board):
                    return True

                board[x][y] = str(0)

        #if False returns, backtracking is needed
        return False
