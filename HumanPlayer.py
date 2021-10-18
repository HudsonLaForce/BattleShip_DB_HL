from Player import Player
from Grid import Grid

class HumanPlayer(Player):
    def __init__(self):
        Player.__init__(self)

    def placeShip(self, ship, size):
        print("lets place", ship, "that is", size, "long")
        while True:
            shipStartX = int(input("What is the x-value of the ship's start: "))
            shipStartY = int(input("What is the y-value of the ship's start: "))
            direction = input("What direction is the ship facing: ")
            if 0 > shipStartX or shipStartX >= 10 or 0 > shipStartY or shipStartY >= 10:
                print("invalid start position")
                continue
            if direction == "up":
                if shipStartY - size < 0:
                    print("ship goes out of grid")
                    continue
            elif direction == "down":
                if shipStartY + size >= 10:
                    print("ship goes out of grid")
                    continue
            elif direction == "left":
                if shipStartX - size < 0:
                    print("ship goes out of grid")
                    continue
            elif direction == "right":
                if shipStartX + size >= 10:
                    print("ship goes out of grid")
                    continue
            else:
                print("invalid direction")
                continue

            shipInWay = False
            for i in range(size):
                if direction == "up" and not self.gridShips.isSpaceWater(shipStartX, shipStartY - i):
                    print("ship in the way")
                    shipInWay = True
                    break
                elif direction == "down" and not self.gridShips.isSpaceWater(shipStartX, shipStartY + i):
                    print("ship in the way")
                    shipInWay = True
                    break
                elif direction == "left" and not self.gridShips.isSpaceWater(shipStartX - i, shipStartY):
                    print("ship in the way")
                    shipInWay = True
                    break
                elif direction == "right" and not self.gridShips.isSpaceWater(shipStartX + i, shipStartY):
                    print("ship in the way")
                    shipInWay = True
                    break
            if shipInWay:
                continue
            break

        if direction == "down":
            self.gridShips.changeCol(shipStartY, ship, shipStartX, size)
        elif direction == "up":
            self.gridShips.changeCol(shipStartY, ship, shipStartX - size + 1, size)
        elif direction == "left":
            self.gridShips.changeRow(shipStartX - size + 1, ship, shipStartY, size)
        elif direction == "right":
            self.gridShips.changeRow(shipStartX, ship, shipStartY, size)
        self.gridShips.printGrid()



    def takeTurn(self, otherPlayer):
        pass