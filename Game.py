class Game:
    def __init__(self, p1, p2):
        self.player1 = p1
        self.player2 = p2


    def playGame(self):
        self.player1.createShipGrid()
        self.player2.createShipGrid()
        while self.player1.stillHasShips() and self.player1.stillHasShips():
            self.player1.takeTurn()
            self.player1.printGrids()
            self.player2.takeTurn()
            self.player2.printGrids()

        if(self.player1.stillHasShips()):
            return "Human PLayer wins"
        else:
            return "Computer PLayer wins"
