# -*- encoding: utf-8 -*-

SYMBOLS = {
  'white R': u'♜', 'white N': u'♞', 'white B': u'♝', 'white Q': u'♛',
  'white K': u'♚', 'white P': u'♟', 'black R': u'♖', 'black N': u'♘',
  'black B': u'♗', 'black Q': u'♕', 'black K': u'♔', 'black P': u'♙'
}

HORIZONTAL_AND_VERTICAL_DIRS = [
 [-1, 0],
 [0, -1],
 [0, 1],
 [1, 0]
]

DIAGONAL_DIRS = [
 [-1, -1],
 [-1, 1],
 [1, -1],
 [1, 1]
]

class Piece(object):
    def __init__(self, board, color, pos):
        self.color = color
        self.board = board
        self.pos = pos

    # def valid_moves(self):
    #     return
class NullPiece(Piece):
    def __init__(self, board):
        Piece.__init__(self, board, None, None)
        self.symbol = ' '

class Slideable(Piece):
    def __init__(self, board, color, pos, move_dirs):
        Piece.__init__(self, board, color, pos)
        self.move_dirs = move_dirs

    def moves(self):
        result = []

        for move_dir in move_dirs:
            move = [self.pos[0] + move_dir[0], self.pos[1] - move_dir[1]]
            while board.can_move(self.color, move):
                result.append(move)
                move = [self.pos[0] + move_dir[0], self.pos[1] - move_dir[1]]

        return result

class Rook(Slideable):
    def __init__(self, board, color, pos):
        Slideable.__init__(self, board, color, pos, HORIZONTAL_AND_VERTICAL_DIRS)
        self.symbol = SYMBOLS[color + " R"]

    def valid_positions(self):
        return [[1, 2]]

class Bishop(Slideable):
    def __init__(self, board, color, pos):
        Slideable.__init__(self, board, color, pos, DIAGONAL_DIRS)
        self.symbol = SYMBOLS[color + " B"]

class Queen(Slideable):
    def __init__(self, board, color, pos):
        Slideable.__init__(self, board, color, pos, DIAGONAL_DIRS + HORIZONTAL_AND_VERTICAL_DIRS)
        self.symbol = SYMBOLS[color + " Q"]


class Knight(Piece):
        def __init__(self, board, color, pos):
            Piece.__init__(self, board, color, pos)
            self.symbol = SYMBOLS[color + " N"]

class King(Piece):
    def __init__(self, board, color, pos):
        Piece.__init__(self, board, color, pos)
        self.symbol = SYMBOLS[color + " K"]

class Pawn(Piece):
    def __init__(self, board, color, pos):
        Piece.__init__(self, board, color, pos)
        self.symbol = SYMBOLS[color + " P"]
