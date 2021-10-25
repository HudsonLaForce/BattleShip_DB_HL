import random
from Shot import Shot
from Player import Player
class ComputerPlayer(Player):
    def __init__(self):
        self.ships = {
            "A" : "Aircraft Carrier" ,
            "B" : "BattleShip" ,
            "C" : "Cruiser" ,
            "S" : "Submarine" ,
            "D" : "Destroyer"
        }
        Player.__init__(self)
        self.shotList = []

    def takeTurn(self, otherPlayer):
        if self.shotList[-1].getResult() == "s":
            self.randTurn(otherPlayer)
        else:
            pass

    #takes the players turn
    # otherPLayer param the opponent who's ship grid will be checked and updated
    def randTurn(self,otherPlayer):
        guess = random.randrange(0,100)
        while (not self.gridShots.isSpaceWater(guess//10,guess%10)):#makes sure guess is not one previously guessed
            guess = random.randrange(0, 100)
        if otherPlayer.gridShips.returnLocation(guess//10,guess%10) != "~":#if guess is not water
            print("hit")
            self.gridShots.changeSingleSpace(guess//10,guess%10,"h")
            shipHit = otherPlayer.gridShips.returnLocation(guess // 10, guess % 10)
            otherPlayer.gridShips.changeSingleSpace(guess // 10, guess % 10, "h")
            for row in range(10):#traverses grid
                for col in range(10):#traverses grid
                    if otherPlayer.gridShips.returnLocation(row,col) == shipHit:#if any spaces a lef of the ship that was hit ends turn
                        self.shipList.append(Shot("h", guess // 10, guess % 10))
                        return otherPlayer.stillHasShips()
            print("you sunk the opponents " + self.ships[shipHit])
            self.shipList.append(Shot("s",guess//10,guess%10))
        else:#miss
            print("miss")
            self.gridShots.changeSingleSpace(guess // 10, guess % 10, "m")
            otherPlayer.gridShips.changeSingleSpace(guess // 10, guess % 10, "m" )
            self.shipList.append(Shot("m", guess // 10, guess % 10))
        return otherPlayer.stillHasShips()
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
                if self.gridShips.returnLocation(row,col) != "~" and self.gridShips.returnLocation(row,col) != "h" and self.gridShips.returnLocation(row,col) != "m":#if a ship is found returns true
                    return True
        return False
