class SudokuBrain:
    """
    @param board: the board
    @return: whether the Sudoku is valid
    """
    def isValidSudoku(self, board):
        #check rows
        for row in board:
            rowString = "".join(row)
            for chr in rowString:
                if chr.isnumeric():
                    testSplit = rowString.split(chr)
                    if len(testSplit) != 2:
                        return False
        #get col
        for colNum in range(9):
            colString = board[0][colNum] + board[1][colNum] + board[2][colNum] + board[3][colNum] + board[4][colNum] + board[5][colNum] + board[6][colNum] + board[7][colNum] + board[8][colNum]
            for chr in colString:
                if chr.isnumeric():
                    testSplit = colString.split(chr)
                    if len(testSplit) != 2:
                        return False
        #check 9 grid
        coords = [(0, 0), (0, 3), (0, 6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]
        for x,y in coords:
       
            gridString = board[x][y] + board[x][y+1] + board[x][y+2] + \
                         board[x+1][y] + board[x+1][y+1] + board[x+1][y+2]+ \
                         board[x+2][y] + board[x+2][y+1] + board[x+2][y+2]
            for chr in gridString:
                if chr.isnumeric():
                    testSplit = gridString.split(chr)
                    if len(testSplit) != 2:
                        return  False
        return True

    def solveSudoku(self, board):
        zeros = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    zeros.append((i, j))
                    
        self.dfs(board, zeros, [False])

        return board
                    
    
    def dfs(self, board, zeros, done):
        
        if len(zeros) == 0: #base case
            done[0] = True
            return
    
        r, c = zeros.pop()
        
        rowValueSet, colValueSet, sepValueSet = set(), set(), set()
        for z in range(0, 9):
            if board[r][z] > 0:
                rowValueSet.add(board[r][z])
            if board[z][c] > 0:
                colValueSet.add(board[z][c])
                
        xOffSet, yOffSet = (r // 3)*3, (c // 3)*3
        for x, y in [(0,0),(0,1),(0,2), (1,0),(1,1),(1,2), (2,0), (2,1), (2,2)]:
            xC, yC = x + xOffSet, y + yOffSet
            if board[xC][yC] > 0:
                sepValueSet.add(board[xC][yC])
            
        for i in range(1, 10):
            if i not in rowValueSet and i not in colValueSet \
            and i not in sepValueSet:
                board[r][c] = i
                self.dfs(board, zeros, done)
                if done[0] == True:
                    break #the for loop
        
        if done[0] == False: #not done yet, and 1 - 9 cannot find solution, so backtrack
            zeros.append((r,c)) #restore before backtracking
            board[r][c] = 0 #restore before backtracking