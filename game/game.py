from player import Player
from puzzle import Puzzle
from drawer import Drawer

class Game():
    def __init__(self):
        self.draw = Drawer()
        self.player = Player()
        self.puzzle = Puzzle()
    
    def startGame(self):
        turno = 0
        while (turno < self.puzzle.leng):
            self.puzzle.printPuzzle(turno)

            turno = turno + 1