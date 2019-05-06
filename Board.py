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

        if turn_color != piece_at_start.color:
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

    def init_piece(self, piece, color, pos):
        return piece(self, color, pos)

    def fill_back_row(self, color):
        pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        row = 0 if color == "white" else 7
        self.rows[row] = [self.init_piece(piece, color, [col, row]) for piece, col in zip(pieces, range(8))]

    def fill_front_row(self, color):
        row = 1 if color == "white" else 6
        self.rows[row] = [self.init_piece(Pawn, color, [col, row]) for col in range(8)]

    def initialize_rows(self):
        def fill_rows(color):
            print self
            self.fill_back_row(color)
            self.fill_front_row(color)

        self.rows = [[NullPiece(self)] * 8 for i in range(8)]
        for color in ["white", "black"]:
            fill_rows(color)
