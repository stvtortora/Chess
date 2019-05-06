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
            #this will be a move on the board and not forcing into check
            move_successful = self.board.make_move(start_pos, end_pos, self.current_player)
            if move_successful:
                self.swap_turn()

        print("{current} is checkmated")

    def swap_turn(self):
        self.current_player = "black" if self.current_player == "white" else "white"



Game().play()
