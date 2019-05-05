from Pieces import Knight
from Pieces import Rook
from Pieces import Bishop
from Pieces import Queen
from Pieces import King
from Pieces import Pawn
from Pieces import NullPiece

class Board:
    def __init__(self):
        self = self
        self.initialize_rows()

    def check_mate(self, player):
        return False

    def make_move(self, start_pos, end_pos):
        print "making move"

    def valid_pos(self, pos):
        return pos[0] < 8 and pos[1] < 8

    def fill_back_row(self, color):
        back_row = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

        for col in range(7):
            if color == "white":
                row = 0
            else:
                row = 7

            piece = back_row[col]
            self.rows[row][col] = piece(self, color, [row, col])

    def fill_front_row(self, color):
        for col in range(7):
            if color == "white":
                row = 1
            else:
                row = 6
            self.rows[row][col] = Pawn(self, color, [row, col])


    def initialize_rows(self):
        self.rows = [[NullPiece(self)] * 8 for i in range(8)]
        # print(self.rows)
        self.fill_back_row("white")
        self.fill_back_row("black")
        self.fill_front_row("white")
        self.fill_front_row("black")
