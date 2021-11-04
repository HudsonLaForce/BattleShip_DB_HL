from HumanPlayer import HumanPlayer
from ComputerPlayer import ComputerPlayer
from Game import Game

# while hp.takeTurn and cp.takeTurn
#print('\033[0;34m ~')

"""
HP = HumanPlayer()
CP = ComputerPlayer()
g = Game(HP,CP)
g.playGame()
"""

CP1 = ComputerPlayer()
CP2 = ComputerPlayer()
g = Game(CP1,CP2)
g.playGame()
