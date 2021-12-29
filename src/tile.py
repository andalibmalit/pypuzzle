from typing import List

class Tile :
    __number, __dim, __sqNum = None
    __coords = [None]*2
    __layout = [None][None]*3

    def __init__(self, int1: int, int2: int, coords: [int]) :
        number = int1
        dim = int2
        newCoords(coords)

    # Getters
    def getX() :
        return coords[0]

    def getY() :
        return coords[1]

    def getNum() :
        return number

    def getSqNum() :
        return sqNum

    def getCoords() :
        return coords

    # Setters
    def updateLay(newLay: [int][int]) :
        layout = newLay

    def move() :
        if (coords[0] - 1 > -1 and layout[coords[0] - 1][coords[1]] == 0) :
            temp = [(coords[0] - 1), coords[1]]
            newCoords(temp)
            return true
        elif (coords[0] + 1 < dim and layout[coords[0] + 1][coords[1]] == 0) :
            temp = [(coords[0] + 1), coords[1]]
            newCoords(temp)
            return true
        elif (coords[1] - 1 > -1 and layout[coords[0]][coords[1] - 1] == 0) :
            temp = [coords[0], (coords[1] - 1)]
            newCoords(temp)
            return true
        elif (coords[1] + 1 < dim and layout[coords[0]][coords[1] + 1] == 0) :
            temp = [coords[0], (coords[1] + 1)]
            newCoords(temp)