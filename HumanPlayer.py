from Player import Player
from Grid import Grid

class HumanPlayer(Player):
    def __init__(self):
        Player.__init__(self)

    def placeShip(self, ship, size):
        illegalPlacement = False
        while(illegalPlacement):
            shipStartX = int(input("What is the x-value of the ship's start: "))
            shipStartY = int(input("What is the x-value of the ship's start: "))
            direction = input("What direction is the ship facing: ")
            if direction != size or

        Grid.changeCol()


    def takeTurn(self):
        pass