import random
from Player import Player
class ComputerPlayer(Player):
    def __init__(self):
        Player.__init__(self)

    def takeTurn(self,otherPlayer):
        guess = random.randrange(0,100)
        while (not self.gridShots.isSpaceWater(guess//10,guess%10)):
            guess = random.randrange(0, 100)
        if otherPlayer.gridShips.returnLocation(guess//10,guess%10) != "~":
            print("hit")
            self.gridShots.changeSingleSpace(guess//10,guess%10,"h")
            for row in otherPlayer.gridShips:
                for col in otherPlayer.gridShips[row]:
                    if otherPlayer.gridShips.returnLocation(row,col) == otherPlayer.gridShips.returnLocation(guess//10,guess%10):
                        if self.gridShots.returnLocation(row,col) != "h":
                            return
            print("you sunk " + str(otherPlayer.gridShips.returnLocation(guess//10,guess%10)))
        else:
            print("miss")
            self.gridShots.changeSingleSpace(guess // 10, guess % 10, "m")

    def placeShip(self, ship, size):
        if(random.randrange(0,2)==1):
            startColumn = random.randrange(0,11-size)
            startRow = random.randrange(0,10)
            for a in range(size):
                if(not self.gridShips.isSpaceWater(startRow,startColumn+a)):
                    return self.placeShip(ship,size)
            for b in range(size):
                self.gridShips.changeSingleSpace(startRow, startColumn+b, ship)
        else:
            startColumn = random.randrange(0, 10)
            startRow = random.randrange(0, 11 - size)
            for a in range(size):
                if (not self.gridShips.isSpaceWater(startRow+a, startColumn)):
                    return self.placeShip(ship, size)
            for b in range(size):
                self.gridShips.changeSingleSpace(startRow + b, startColumn, ship)


