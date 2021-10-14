from Player import Player
from Grid import Grid

class HumanPlayer(Player):
    def __init__(self):
        Player.__init__(self)

    def placeShip(self, ship, size):
        illegalPlacement = True
        while(True):
            shipStartX = int(input("What is the x-value of the ship's start: "))
            shipStartY = int(input("What is the x-value of the ship's start: "))
            direction = input("What direction is the ship facing: ")
            if 0 > shipStartX >= 10 or 0 > shipStartY >= 10:
                print("invalid entry")
                continue
            if direction == "up":
                if shipStartY - size < 0:
                    print("invalid entry")
                    continue
            elif direction == "down":
                if shipStartY + size >= 10:
                    print("invalid entry")
                    continue
            elif direction == "left":
                if shipStartX - size < 0:
                    print("invalid entry")
                    continue
            elif direction == "right":
                if shipStartX + size >= 10:
                    print("invalid entry")
                    continue
            else:
                continue

            for i in range(size):
                if direction == "up":
                    illegalPlacement = not self.gridShips.isSpaceWater(shipStartX, shipStartY - i)
                elif direction == "down":
                    illegalPlacement = not self.gridShips.isSpaceWater(shipStartX, shipStartY + i)
                elif direction == "left":
                    illegalPlacement = not self.gridShips.isSpaceWater(shipStartX - i, shipStartY)
                elif direction == "right":
                    illegalPlacement = not self.gridShips.isSpaceWater(shipStartX + i, shipStartY)
                else:
                    illegalPlacement = True


        Grid.changeCol()


    def takeTurn(self, otherPlayer):
        pass