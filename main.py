from Grid import Grid

from ComputerPlayer import ComputerPlayer

grid = Grid()
cp = ComputerPlayer()
grid.printGrid()

cp = ComputerPlayer()
cp.createShipGrid()
cp.printGrids()