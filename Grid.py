class Grid:
    def __init__(self):
        self.grid = [["~","~","~","~","~","~","~","~","~","~"],
                     ["~","~","~","~","~","~","~","~","~","~"],
                     ["~","~","~","~","~","~","~","~","~","~"],
                     ["~","~","~","~","~","~","~","~","~","~"],
                     ["~","~","~","~","~","~","~","~","~","~"],
                     ["~","~","~","~","~","~","~","~","~","~"],
                     ["~","~","~","~","~","~","~","~","~","~"],
                     ["~","~","~","~","~","~","~","~","~","~"],
                     ["~","~","~","~","~","~","~","~","~","~"],
                     ["~","~","~","~","~","~","~","~","~","~"] ]
    # Change a single position
    def changeSingleSpace(self, row, col , value):
        self.grid[row][col] = value

    # Row = the row to change
    # Value = the string to put into the list
    # colStart = the start of the column to be changed
    # size = number of spaces in the column to change
    def changeRow(self , row , value , colStart , size ):
        for col in range( colStart , colStart + size ) :
            self.grid[row][col] = value

    # Col = the col to change
    # Value = the string to put into the list
    # rowStart = the start of the row to be changed
    # size = number of spaces in the row to change
    def changeCol(self , col , value , rowStart , size ):
        for row in range( rowStart , rowStart + size ) :
            self.grid[row][col] = value

    def returnLocation(self , row , col ):
        return self.grid[row][col]

    colors = {
        "~": "\033[1;34m ~ \033[0;0m",
        "m": "\033[1;37m m \033[0;0m",
        "A": "\033[1;33m A \033[0;0m",
        "B": "\033[1;33m B \033[0;0m",
        "C": "\033[1;33m C \033[0;0m",
        "S": "\033[1;33m S \033[0;0m",
        "D": "\033[1;33m D \033[0;0m",
        "h": "\033[1;31m h \033[0;0m"
    }
    def printGrid(self):
        for row in range(len(self.grid)) :
            x = "["
            for col in range(len(self.grid[row])):
                x = x  + self.colors[self.grid[row][col]] + ","
            x = x + "]"
            print(x)
    # This is a useful method to determine if the space is "~" or something else
    # Send it the grid you want to check, so ship or shot
    def isSpaceWater(self, row, col):
        if self.grid[row][col] == "~":
            return True
        else:
            return False
