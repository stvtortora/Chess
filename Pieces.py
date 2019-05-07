# -*- encoding: utf-8 -*-

SYMBOLS = {
  'solid R': u'♜', 'solid N': u'♞', 'solid B': u'♝', 'solid Q': u'♛',
  'solid K': u'♚', 'solid P': u'♟', 'clear R': u'♖', 'clear N': u'♘',
  'clear B': u'♗', 'clear Q': u'♕', 'clear K': u'♔', 'clear P': u'♙'
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

KNIGHT_MOVES =     [
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

    def can_move_to(self, move):
        if self.board.on_board(move):
            piece_found = self.board.piece_at(move)
            return not piece_found or piece_found.color != self.color
        return False

    def valid_moves(self):
        def is_valid_move(move):
            board_copy = self.board.copy()
            board_copy.move_piece(self.pos, move)
            return not board_copy.in_check(self.color)

        return list(filter(lambda move: is_valid_move(move), self.moves()))

class NullPiece(Piece):
    def __init__(self, board, color=None, pos=None):
        Piece.__init__(self, board, color, pos)
        self.symbol = ' '

    def moves(self):
        return []

class Stepable(Piece):
    def __init__(self, board, color, pos, step_options):
        Piece.__init__(self, board, color, pos)
        self.step_options = step_options

    def moves(self):
        def move(step):
            row_step, col_step = step
            return [start_row + row_step, start_col + col_step]

        start_row, start_col = self.pos
        move_options = [move(step_option) for step_option in self.step_options]
        return list(filter(lambda move: self.can_move_to(move), move_options))

class Slideable(Piece):
    def __init__(self, board, color, pos, move_dirs):
        Piece.__init__(self, board, color, pos)
        self.move_dirs = move_dirs

    def moves(self):
        result = []
        start_row, start_col = self.pos

        for move_dir in self.move_dirs:
            row_dir, col_dir = move_dir
            move = self.pos
            can_continue = True

            while can_continue:
                prev_row, prev_col = move
                move = [prev_row + row_dir, prev_col + col_dir]

                can_move = self.can_move_to(move)
                if can_move:
                    result.append(move)
                if not can_move or bool(self.board.piece_at(move)):
                    can_continue = False

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
            Stepable.__init__(self, board, color, pos, KNIGHT_MOVES)
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
        if self.color == "solid":
            return 1
        return -1

    def attack_moves(self):
        def can_attack(pos):
            piece_to_attack = self.board.piece_at(pos)
            return piece_to_attack and piece_to_attack.color != self.color
        row, col = self.pos
        attack_pos = [[row + self.forward_step(), col - 1], [row + self.forward_step(), col + 1]]
        return list(filter(lambda pos: can_attack(pos), attack_pos))

    def forward_moves(self):
        def at_start_pos():
            return self.pos[0] == 1 if self.color == "solid" else self.pos[0] == 6

        def can_forward_step_to(pos):
            return not self.board.piece_at(pos) and self.board.on_board(pos)

        row, col = self.pos
        forward_pos = [[row + self.forward_step(), col]]
        if at_start_pos():
            forward_pos.append([row + self.forward_step() * 2, col])
        return list(filter(lambda pos: can_forward_step_to(pos), forward_pos))
