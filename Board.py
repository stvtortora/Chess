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

    def piece_at(self, pos):
        row, col = pos
        return self.rows[row][col]

    def make_move(self, start_pos, end_pos, turn_color):
        piece_at_start = self.piece_at(start_pos)

        if  != piece_at_start.color:
            print "Thats not your piece"
            return False

        if end_pos in piece_at_start.valid_moves():
            piece_at_end = self.piece_at(end_pos)

            self.rows[start_pos[0]][start_pos[1]] = NullPiece(self)
            self.rows[end_pos[0]][end_pos[1]] = piece_at_start
            piece_at_start.pos = end_pos

            if piece_at_end.symbol:
                piece_at_end.pos = None
            return True

        elif end_pos in piece_at_start.moves():
            print "Cannot move into check"
            return False

        else:
            print "Piece cannot move like that"
            return False

    def valid_pos(self, pos):
        return pos[0] < 8 and pos[1] < 8 and pos[1] > -1 and pos[0] > -1

    def fill_back_row(self, color):
        back_row = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

        for col in range(8):
            if color == "white":
                row = 0
            else:
                row = 7

            piece = back_row[col]
            self.rows[row][col] = piece(self, color, [row, col])

    def fill_front_row(self, color):
        for col in range(8):
            if color == "white":
                row = 1
            else:
                row = 6
            self.rows[row][col] = Pawn(self, color, [row, col])


    def initialize_rows(self):
        self.rows = [[NullPiece(self)] * 8 for i in range(8)]
        self.fill_back_row("white")
        self.fill_back_row("black")
        self.fill_front_row("white")
        self.fill_front_row("black")
