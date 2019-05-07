from Board import Board
from Display import Display
from HumanPlayer import HumanPlayer
from ComputerPlayer import ComputerPlayer

class Game:
    def __init__(self):
        self = self
        self.board = Board()
        self.display = Display(self.board)
        self.players = {
            "white": HumanPlayer("white", self.display),
            "black": ComputerPlayer("black", self.display)
        }
        self.current_player = "white"

    def play(self):
        check_mate, stale_mate = False, False
        while not check_mate and not stale_mate:
            start_pos, end_pos = self.players[self.current_player].get_move()
            move_successful = self.board.make_move(start_pos, end_pos, self.current_player)

            if move_successful:
                self.swap_turn()
                check_mate, stale_mate = self.board.mate(self.current_player)

        self.display.render()
        print(f'{self.current_player} is {"checkmated" if check_mate else "stalemated"}')

    def swap_turn(self):
        self.current_player = "black" if self.current_player == "white" else "white"



Game().play()
