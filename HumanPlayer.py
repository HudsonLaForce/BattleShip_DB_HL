from Player import Player
from Grid import Grid

class HumanPlayer(Player):
    def __init__(self):
        Player.__init__(self)

    def placeShip(self, ship, size):
        print("Place", ship, "that is", size, "squares long")
        while True:
            shipStartRow = int(input("What is the row of the ship's start: "))
            shipStartCol = int(input("What is the column of the ship's start: "))
            direction = input("What direction is the ship facing: ")
            if not (0 <= shipStartRow <= 9 and 0 <= shipStartCol <= 9):
                print("Invalid start position")
                continue
            if direction == "up":
                if shipStartRow - size < 0:
                    print("Ship goes out of grid")
                    continue
            elif direction == "down":
                if shipStartRow + size >= 10:
                    print("Ship goes out of grid")
                    continue
            elif direction == "left":
                if shipStartCol - size < 0:
                    print("Ship goes out of grid")
                    continue
            elif direction == "right":
                if shipStartCol + size >= 10:
                    print("Ship goes out of grid")
                    continue
            else:
                print("Invalid direction")
                continue

            shipInWay = False
            for i in range(size):
                if direction == "up" and not self.gridShips.isSpaceWater(shipStartRow - i, shipStartCol):
                    print("Ship in the way")
                    shipInWay = True
                    break
                elif direction == "down" and not self.gridShips.isSpaceWater(shipStartRow + i, shipStartCol):
                    print("Ship in the way")
                    shipInWay = True
                    break
                elif direction == "left" and not self.gridShips.isSpaceWater(shipStartRow, shipStartCol - i):
                    print("Ship in the way")
                    shipInWay = True
                    break
                elif direction == "right" and not self.gridShips.isSpaceWater(shipStartRow, shipStartCol + i):
                    print("Ship in the way")
                    shipInWay = True
                    break
            if shipInWay:
                continue
            break

        if direction == "down":
            self.gridShips.changeCol(shipStartCol, ship, shipStartRow, size)
        elif direction == "up":
            self.gridShips.changeCol(shipStartCol, ship, shipStartRow - size + 1, size)
        elif direction == "left":
            self.gridShips.changeRow(shipStartRow, ship, shipStartCol - size + 1, size)
        elif direction == "right":
            self.gridShips.changeRow(shipStartRow, ship, shipStartCol, size)
        self.gridShips.printGrid()

    def takeTurn(self, otherPlayer):
        self.gridShots.printGrid()
        while True:
            shotRow = int(input("What is the row of your shot"))
            shotCol = int(input("What is the column of your shot"))
            if not (0 <= shotRow <= 9 and 0 <= shotCol <= 9):
                print("Invalid shot position")
                continue
            elif not self.gridShots.isSpaceWater(shotRow, shotCol):
                print("You have already shot here")
                continue
            else:
                break

        if otherPlayer.gridShips.isSpaceWater(shotRow, shotCol):
            print("miss")
            self.gridShots.changeSingleSpace(shotRow, shotCol, "m")
            return False
        else:
            print("hit")
            self.gridShots.changeSingleSpace(shotRow, shotCol, "h")
            otherPlayer.gridShips.changeSingleSpace(shotRow, shotCol, "h")
            sunk = True
            hitShip = otherPlayer.gridShips.returnLocation(shotRow, shotCol)
            for row in otherPlayer.gridShips:
                for col in otherPlayer.gridShips[row]:
                    if otherPlayer.gridShips.returnLocation(row, col) == hitShip: sunk = True
            if sunk:
                print("you sunk", hitShip, "!")
            return otherPlayer.stillHasShips()

    def stillHasShips(self):
        for row in self.gridShips:
            for col in self.gridShip[row]:
                if self.gridShips.returnLocation(row, col) != "~" or "h" or "m":
                    return True



