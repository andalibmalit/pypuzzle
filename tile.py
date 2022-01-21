class Tile :
    __number = None
    __dim = None
    __sqNum = None
    __coords = [None]*2
    __gameState = None

    def __init__(self, int1, int2, coords) :
        self.__number = int1
        self.__dim = int2
        self.__coords = coords
        self.calcSqNum()


    # Getters
    def x(self) :
        return self.__coords[0]

    def y(self) :
        return self.__coords[1]

    def getNum(self) :
        return self.__number

    def getSqNum(self) :
        return self.__sqNum

    def getCoords(self) :
        return self.__coords


    # Setters
    def newGameState(self, gameState) :
        self.__gameState = gameState

    def move(self) :
        x = self.__coords[0]
        y = self.__coords[1]
        board = self.__gameState
        dim = self.__dim

        if x - 1 > -1 and board[x - 1][y] == 0 :
            coords = [x - 1, y]
            self.__coords = coords
            self.calcSqNum()
            return True
        elif x + 1 < dim and board[x + 1][y] == 0 :
            coords = [x + 1, y]
            self.__coords = coords
            self.calcSqNum()
            return True
        elif y - 1 > -1 and board[x][y - 1] == 0 :
            coords = [x, y - 1]
            self.__coords = coords
            self.calcSqNum()
            return True
        elif y + 1 < dim and board[x][y + 1] == 0 :
            coords = [x, y + 1]
            self.__coords = coords
            self.calcSqNum()
            return True
        # If Tile object is immovable in current game state
        else : 
            return False

    # See README for details on formula to find square number of a Tile
    def calcSqNum(self) :
    	self.__sqNum = self.__coords[0] * self.__dim + self.__coords[1] + 1


    # Debugging
    def __str__(self) :
        t = "TILE " + str(self.__number) + ": " + "\n" + "(" + str(self.__coords[0]) + ", " + str(self.__coords[1]) + ")" + "\n" + "sqNum: " + str(self.__sqNum) + "\n"
        return t