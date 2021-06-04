
class PuzzleState:
    def __init__(self, numbers):
        #initialize the data
        self.cells=[]
        self.blankLocation = 0, 0
        #[0,1,2,3,4,5,6,7,8]
        k= 0
        for i in range(3):
            row=[]
            for j in range(3):
                row.append(numbers[k])
                if numbers[k]==0:
                    self.blankLocation= i,j
                k +=1
            self.cells.append(row)

    def printState(self):
        #print the current state
        lines = []
        horizontalline = ("_" * (13))
        print(horizontalline)
        for row in self.cells:
            rowline ="|"
            for col in row:
                if col == 0:
                    col = "."
                rowline = rowline +" " + col.__str__() + "|"
            print(rowline)
            print(horizontalline)
    
    def isGoal(self):
        #check is the state is goal or not
        current = 0
        for i in range(3):
            for j in range(3):
                if current !=self.cells[i][j]:
                    return False
                current +=1
        return True
    
    def legalMoves(self):
        #return all the legal mover 
        row, col = self.blankLocation
        legalMoves=[]
        if row != 0:
            legalMoves.append("up")
        if row !=2:
            legalMoves.append("down")
        if col != 0:
            legalMoves.append("left")
        if col !=2:
            legalMoves.append("right")
        return legalMoves

    def resultState(self, move):
        #return the next state based the move
        row, col = self.blankLocation
        if move == "up":
            newrow = row-1
            newcol = col
        elif move == "down":
            newrow = row +1
            newcol = col
        elif move == "left":
            newrow = row
            newcol = col-1
        elif move =="right":
            newrow = row 
            newcol = col+1
        else:
            raise "ilegal move"

        newPuzzle = PuzzleState([0,0,0,0,0,0,0,0,0])
        newPuzzle.cells = [value[:] for value in self.cells]
        #new puzzle cells
        newPuzzle.cells[row][col] = self.cells[newrow][newcol]
        newPuzzle.cells[newrow][newcol] = self.cells[row][col]

        newPuzzle.blankLocation = newrow, newcol
        return newPuzzle
    
    def __eq__(self, other):
        for row in range(3):
            if self.cells[row] != other.cells[row]:
                return False
        return True

    
class SearchProblem:
    def __init__(self, state):
        # initialize the search problem
        self.puzzle = state

    def getStartState(self):
        # return the chile state
        return self.puzzle

    def getSuccessor(self,state):
        #retrun all the child state
        succs = []
        
        for move in state.legalMoves():
            cState = state.resultState(move)
            succs.append((cState, move))
        return succs

    def isGoalState(self, state):
        #return information that state is goal or not
        return state.isGoal()
#calculating distance by manhatan formula

def mdistatance(xy1, xy2):
    
    return abs(xy1[0]-xy2[0]) + abs(xy1[1]-xy2[1])

goal = {0:(0,0), 1:(0,1), 2:(0,2), 3:(1,0), 4:(1,1), 5:(1,2), 6:(2,0), 7:(2,1), 8:(2,2)}
# checking for the heightest point if start decreasing
#  then it we move and if again start icreasing it should stop
def hvalue(state):
    hscore = 0
    for row in range(3):
        for col in range(3):
            if state.cells[row][col] == 0:
                continue
            goal1 = goal[state.cells[row][col]]
            xy1 = (row, col)
            hscore += mdistatance(xy1, goal1)
    return hscore
