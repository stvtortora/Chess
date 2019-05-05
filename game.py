from Board import Board
from Display import Display
from HumanPlayer import HumanPlayer

class Game:
    def __init__(self):
        self = self
        self.board = Board()
        self.display = Display(self.board)
        self.players = {
            "white": HumanPlayer("white", self.display),
            "black": HumanPlayer("black", self.display)
        }
        self.current_player = "white"

    def play(self):

        while not self.board.check_mate(self.current_player):
            start_pos, end_pos = self.players[self.current_player].get_move()
            self.display.render()
            self.board.make_move(start_pos, end_pos)
            self.swap_turn()
        print ("{current} is checkmated")

    def swap_turn(self):
        if self.current_player == "white":
            self.current_player = "black"
        else:
            self.current_player = "white"



Game().play()
