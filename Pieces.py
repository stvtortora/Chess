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

KNIGHT_DIRS =     [
    [-2, -1],
    [-1, -2],
    [-2, 1],
    [-1, 2],
    [1, -2],
    [2, -1],
    [1, 2],
    [2, 1]
]

class Piece(object):
    def __init__(self, board, color, pos):
        self.color = color
        self.board = board
        self.pos = pos

    def valid_moves(self):
        print self.moves()
        return self.moves()

    # def valid_moves(self):
    #     return
class NullPiece(Piece):
    def __init__(self, board):
        Piece.__init__(self, board, None, None)
        self.symbol = ' '

class Stepable(Piece):
    def __init__(self, board, color, pos, move_dirs):
        Piece.__init__(self, board, color, pos)
        self.move_dirs = move_dirs

class Slideable(Piece):
    def __init__(self, board, color, pos, move_dirs):
        Piece.__init__(self, board, color, pos)
        self.move_dirs = move_dirs

    def moves(self):
        result = []

        for move_dir in move_dirs:
            move = [self.pos[0] + move_dir[0], self.pos[1] + move_dir[1]]
            piece_found = None

            while not piece_found:
                piece_found = board.piece_at(move)
                if not piece_found or piece_found.color != self.color:
                    result.append(move)
                move = [move[0] + move_dir[0], move[1] + move_dir[1]]

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


class Knight(Stepable):
        def __init__(self, board, color, pos):
            Stepable.__init__(self, board, color, pos, KNIGHT_DIRS)
            self.symbol = SYMBOLS[color + " N"]

class King(Stepable):
    def __init__(self, board, color, pos):
        Stepable.__init__(self, board, color, pos, DIAGONAL_DIRS + HORIZONTAL_AND_VERTICAL_DIRS)
        self.symbol = SYMBOLS[color + " K"]

class Pawn(Piece):
    def __init__(self, board, color, pos):
        Piece.__init__(self, board, color, pos)
        self.symbol = SYMBOLS[color + " P"]

    def moves(self):
        return self.attack_moves() + self.forward_moves()

    def forward_step(self):
        if self.color == "white":
            return 1
        return -1

    def at_start_pos(self):
        if self.color == "white":
            return self.pos[0] == 1
        return self.pos[0] == 6

    def can_attack(self, pos):
        piece_to_attack_color = self.board.piece_at(pos).color
        return self.board.valid_pos(pos) and piece_to_attack_color and piece_to_attack_color != self.color

    def can_move_to(self, pos):
        return bool(self.board.piece_at(pos).color)

    def attack_moves(self):
        row, col = self.pos
        attack_pos = [[row + self.forward_step(), col - 1], [row + self.forward_step(), col + 1]]
        return list(filter(lambda pos: self.can_attack(pos), attack_pos))

    def forward_moves(self):
        row, col = self.pos
        forward_pos = [[row + self.forward_step(), col]]
        if self.at_start_pos():
            forward_pos.append([row + self.forward_step() * 2, col])
        return list(filter(lambda pos: self.can_move_to(pos), forward_pos))
