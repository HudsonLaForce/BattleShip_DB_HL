from Player import Player


class HumanPlayer(Player):
    def __init__(self):
        Player.__init__(self)
    """
    this method places a ship into the grid
    ship: a string with the ship token
    size: the length of the ship
    """
    def placeShip(self, ship, size):
        print("Place", ship, "that is", size, "squares long")
        while True: # runs until broken from inside
            shipStartRow = int(input("What is the row of the ship's start: "))
            shipStartCol = int(input("What is the column of the ship's start: "))
            if not (0 <= shipStartRow <= 9 and 0 <= shipStartCol <= 9): # if the input is outside the grid
                print("Invalid start position")
                continue
            direction = input("What direction is the ship facing: ")
            if direction == "up":  # if the direction is up
                if shipStartRow - size < 0:  # if ship would go out of grid
                    print("Ship goes out of grid")
                    continue
            elif direction == "down":   # if direction is down
                if shipStartRow + size >= 10:   # if ship would go out of grid
                    print("Ship goes out of grid")
                    continue
            elif direction == "left":   # if direction is left
                if shipStartCol - size < 0:  # if ship would go out of grid
                    print("Ship goes out of grid")
                    continue
            elif direction == "right":  # if direction is right
                if shipStartCol + size >= 10:   # if ship would go out of grid
                    print("Ship goes out of grid")
                    continue
            else:   # if the direction input is invalid
                print("Invalid direction")
                continue

            shipInWay = False
            for i in range(size):   # for every grid the ship should take up
                if direction == "up" and not self.gridShips.isSpaceWater(shipStartRow - i, shipStartCol):
                    print("Ship in the way")    # if there would be a ship in the way in the up direction
                    shipInWay = True
                    break
                elif direction == "down" and not self.gridShips.isSpaceWater(shipStartRow + i, shipStartCol):
                    print("Ship in the way")
                    shipInWay = True    # if there would be a ship in the way in the down direction
                    break
                elif direction == "left" and not self.gridShips.isSpaceWater(shipStartRow, shipStartCol - i):
                    print("Ship in the way")
                    shipInWay = True    # if there would be a ship in the way in the left direction
                    break
                elif direction == "right" and not self.gridShips.isSpaceWater(shipStartRow, shipStartCol + i):
                    print("Ship in the way")
                    shipInWay = True    # if there would be a ship in the right direction
                    break
            if shipInWay:   # if there is a ship in the way
                continue
            break   # if it gets here then the input is valid and exit the loop

        if direction == "down":  # if the ship is facing down
            self.gridShips.changeCol(shipStartCol, ship, shipStartRow, size)
        elif direction == "up":  # if the ship is facing up
            self.gridShips.changeCol(shipStartCol, ship, shipStartRow - size + 1, size)
        elif direction == "left":   # if the ship is facing left
            self.gridShips.changeRow(shipStartRow, ship, shipStartCol - size + 1, size)
        elif direction == "right":  # if the ship is facing right
            self.gridShips.changeRow(shipStartRow, ship, shipStartCol, size)
        self.gridShips.printGrid()

    """
    this method makes the turn for the player
    otherPlayer: the other players whose ship grid will be read and changed
    return: returns whether the player can still make a move after the method runs
    """
    def takeTurn(self, otherPlayer):
        self.gridShots.printGrid()
        while True: # runs until valid input
            shotRow = int(input("What is the row of your shot: "))
            shotCol = int(input("What is the column of your shot: "))
            if not (0 <= shotRow <= 9 and 0 <= shotCol <= 9):   # if the shot is not in the grid
                print("Invalid shot position")
                continue
            elif not self.gridShots.isSpaceWater(shotRow, shotCol):  # if the shot has already been done
                print("You have already shot here")
                continue
            else:   # if its a valid shot
                break

        if otherPlayer.gridShips.isSpaceWater(shotRow, shotCol):    # if the shot is a miss
            print("miss")
            self.gridShots.changeSingleSpace(shotRow, shotCol, "m")
            return True
        else:   # if the shot is a hit
            print("hit")
            self.gridShots.changeSingleSpace(shotRow, shotCol, "h")
            otherPlayer.gridShips.changeSingleSpace(shotRow, shotCol, "h")
            sunk = True
            hitShip = otherPlayer.gridShips.returnLocation(shotRow, shotCol)
            for row in range(10):   # traverse row in grid
                for col in range(10):  # traverse cols in grid
                    if otherPlayer.gridShips.returnLocation(row, col) == hitShip:  # if the ships still in the grid
                        sunk = True
            if sunk:    # if the ship is sunk
                print("you sunk", hitShip, "!")
        return otherPlayer.stillHasShips()

    """
    this method determines if the player still has ships to be sunk
    return: returns whether there still are ships
    """
    def stillHasShips(self):
        for row in range(10):  # traverse rows in grid
            for col in range(10):  # traverse cols in grid
                if self.gridShips.returnLocation(row, col) != "~" and self.gridShips.returnLocation(row, col) != "h" and self.gridShips.returnLocation(row, col) != "m":    # if there still is a ship
                    return True
        return False
