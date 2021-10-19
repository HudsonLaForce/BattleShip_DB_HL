from HumanPlayer import HumanPlayer
from ComputerPlayer import ComputerPlayer
from Game import Game

# while hp.takeTurn and cp.takeTurn

HP = HumanPlayer()
CP = ComputerPlayer()

g = Game(HP,CP)

g.playGame()

