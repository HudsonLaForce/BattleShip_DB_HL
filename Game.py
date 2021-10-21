class Game:
    def __init__(self, p1, p2):
        self.player1 = p1
        self.player2 = p2


    def playGame(self):
        self.player1.createShipGrid()
        self.player2.createShipGrid()

        while self.player1.stillHasShips() and self.player2.stillHasShips():
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Human Computer PLayers Turn")
            if not self.player1.takeTurn(self.player2):
                print("Human Player wins")
                return
            self.player1.printGrids()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Computer Computer PLayers Turn")
            if not self.player2.takeTurn(self.player1):
                print("Computer Player wins")
                return
            self.player2.printGrids()