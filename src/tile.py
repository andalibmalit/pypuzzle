class Tile :
    __number = None
    __dim = None
    __sqNum = None
    __coords = [None]*2
    __layout = None

    def __init__(self, int1, int2, ncoords) :
        self.__number = int1
        self.__dim = int2
        self.newCoords(ncoords)

    # Getters
    def xZero(self) :
        return self.__coords[0]

    def yZero(self) :
        return self.__coords[1]

    def getNum(self) :
        return self.__number

    def getSqNum(self) :
        return self.__sqNum

    def getCoords(self) :
        return self.__coords

    # Setters
    def updateLay(self, newLay) :
        self.__layout = newLay

    def move(self) :
        x = self.__coords[0]
        y = self.__coords[1]

        if x - 1 > -1 and layout[x - 1][y] == 0 :
            temp = [x - 1, y]
            self.__newCoords(temp)
            return true
        elif x + 1 < dim and layout[x + 1][y] == 0 :
            temp = [x + 1, y]
            self.__newCoords(temp)
            return true
        elif y - 1 > -1 and layout[x][y - 1] == 0 :
            temp = [x, y - 1]
            self.__newCoords(temp)
            return true
        elif y + 1 < dim and layout[x][y + 1] == 0 :
            temp = [x, y + 1]
            self.__newCoords(temp)
            return true
        else : return false

    def newCoords(self, newC) :
        self.__coords = newC
        self.calcSqNum()

    def calcSqNum(self) :
    	self.__sqNum = self.__coords[0] * self.__dim + self.__coords[0] + 1
        # if coords[0] == 0 :
        #    sqNum = coords[1] + 1
        # elif coords[1] = 0 :
        #    sqNum = coords[0] * dim + 1
        # else :
        #    sqNum = coords[0] * dim + coords[1] + 1