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
            if 0 > shipStartRow or shipStartRow >= 10 or 0 > shipStartCol or shipStartCol >= 10:
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
        pass