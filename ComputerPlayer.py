import random
from Player import Player
class ComputerPlayer(Player):
    def __init__(self):
        Player.__init__(self)

    #takes the players turn
    # otherPLayer param the opponent who's ship grid will be checked and updated
    def takeTurn(self,otherPlayer):
        guess = random.randrange(0,100)
        while (not self.gridShots.isSpaceWater(guess//10,guess%10)):#makes sure guess is not one previously guessed
            guess = random.randrange(0, 100)
        if otherPlayer.gridShips.returnLocation(guess//10,guess%10) != "~":#if guess is not water
            print("hit")
            self.gridShots.changeSingleSpace(guess//10,guess%10,"h")
            shipHit = otherPlayer.gridShips.returnLocation(guess // 10, guess % 10)
            otherPlayer.gridShips.changeSingle(guess // 10, guess % 10, "h")
            for row in otherPlayer.gridShips:#traverses grid
                for col in otherPlayer.gridShips[row]:#traverses grid
                    if otherPlayer.gridShips.returnLocation(row,col) == shipHit:#if any spaces a lef of the ship that was hit ends turn
                        return self.stillHasShips()
            print("you sunk the opponents " + shipHit)
        else:#miss
            print("miss")
            self.gridShots.changeSingleSpace(guess // 10, guess % 10, "m")
            otherPlayer.gridShips.changeSingle(guess // 10, guess % 10, "m" )
        return self.stillHasShips()
    #places a ship in the Computer Players shipGrid
    #ship param a letter representing what ship is being placed
    #size param the number of spaces that the ship takes up
    def placeShip(self, ship, size):
        if(random.randrange(0,2)==1):#picks horizontal or vertical
            startColumn = random.randrange(0,11-size)
            startRow = random.randrange(0,10)
            for a in range(size):#checks every space that the ship will take up
                if(not self.gridShips.isSpaceWater(startRow,startColumn+a)):#checks for enough open spaces
                    return self.placeShip(ship,size)
            for b in range(size):#places ship
                self.gridShips.changeSingleSpace(startRow, startColumn+b, ship)
        else:#Vertical
            startColumn = random.randrange(0, 10)
            startRow = random.randrange(0, 11 - size)
            for a in range(size):#checks every space that the ship will take up
                if (not self.gridShips.isSpaceWater(startRow+a, startColumn)):#checks for enough open spaces
                    return self.placeShip(ship, size)
            for b in range(size):#places ship
                self.gridShips.changeSingleSpace(startRow + b, startColumn, ship)

    # this method will determine if the Player's ship grid still
    # has ships or not
    # If they have no ships left, the other player wins
    # This method returns true if they still have ships
    # This method returns false if they don't have ships
    def stillHasShips(self):
        for row in range(10):#traverses grid
            for col in range(10):#traverses grid
                if self.gridShips.returnLocation(row,col) != "~" or "h" or "m":#if a ship is found returns true
                    return True
        return False