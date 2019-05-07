from Pieces import Knight, Rook, Bishop, Queen, King, Pawn, NullPiece

class Board:
    def __init__(self):
        self.initialize_rows()

    def mate(self, color):
        for row in self.rows:
            for piece in row:
                if piece.color == color and len(piece.valid_moves()) > 0:
                    return False, False

        check_mate = self.in_check(color)
        stale_mate = not check_mate
        return check_mate, stale_mate



    def king_pos(self, color):
        for row, i in zip(self.rows, range(8)):
            for piece, j in zip(row, range(8)):
                if isinstance(piece, King) and piece.color == color:
                    return i, j
        return None

    def in_check(self, color):
        king_row, king_col = self.king_pos(color)
        opponent = "solid" if color == "clear" else "clear"
        for row in self.rows:
            for piece in row:
                if piece.color == opponent:
                    for move in piece.moves():
                        if move[0] == king_row and move[1] == king_col:
                            return True
        return False

    def piece_at(self, pos):
        row, col = pos
        return None if not self.on_board(pos) or not self.rows[row][col].color else self.rows[row][col]

    def copy(self):
        def row_copy(row):
            def piece_copy(piece):
                piece_type = type(piece)
                return piece_type(board_copy, piece.color, None if not piece.pos else piece.pos.copy())

            return [piece_copy(piece) for piece in row]

        board_copy = Board()
        board_copy.rows = [row_copy(row) for row in self.rows]
        return board_copy

    def move_piece(self, start_pos, end_pos):
        piece_at_start = self.piece_at(start_pos)
        piece_at_end = self.piece_at(end_pos)

        self.rows[start_pos[0]][start_pos[1]] = NullPiece(self)
        self.rows[end_pos[0]][end_pos[1]] = piece_at_start
        piece_at_start.pos = end_pos

        if piece_at_end:
            piece_at_end.pos = None

    def make_move(self, start_pos, end_pos, turn_color):
        piece_at_start = self.piece_at(start_pos)

        if not piece_at_start:
            print("There must be a piece at the positon you move from")
            return False

        if turn_color != piece_at_start.color:
            print("Thats not your piece")
            return False

        if end_pos in piece_at_start.valid_moves():
            self.move_piece(start_pos, end_pos)
            return True

        elif end_pos in piece_at_start.moves():
            print("Cannot move into check")
            return False

        else:
            print("Piece cannot move like that")
            return False

    def on_board(self, pos):
        return pos[0] < 8 and pos[1] < 8 and pos[1] > -1 and pos[0] > -1

    def init_piece(self, piece, color, pos):
        return piece(self, color, pos)

    def fill_back_row(self, color):
        pieces = (Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook)
        row = 0 if color == "solid" else 7
        self.rows[row] = [self.init_piece(piece, color, [row, col]) for piece, col in zip(pieces, range(8))]

    def fill_front_row(self, color):
        row = 1 if color == "solid" else 6
        self.rows[row] = [self.init_piece(Pawn, color, [row, col]) for col in range(8)]

    def initialize_rows(self):
        def fill_rows(color):
            self.fill_back_row(color)
            self.fill_front_row(color)

        self.rows = [[NullPiece(self)] * 8 for i in range(8)]
        for color in ["solid", "clear"]:
            fill_rows(color)
