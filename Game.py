class Game:
    def __init__(self, p1, p2):
        self.player1 = p1
        self.player2 = p2


    def playGame(self):
        self.player1.createShipGrid()
        self.player2.createShipGrid()
        turns = 0
        while self.player1.stillHasShips() and self.player2.stillHasShips():
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Human Players Turn")
            if not self.player1.takeTurn(self.player2):
                print("Human Player wins")
                break
            self.player1.printGrids()
            #x = input("continue?")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Computer Players Turn")
            if not self.player2.takeTurn(self.player1):
                print("Computer Player wins")
                break
            turns += 1
            self.player2.printGrids()#commment out later
            #x = input("continue?")
        print(turns)