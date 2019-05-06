from Cursor import Cursor

class Display:
    def __init__(self, board):
        self.board = board
        self.cursor = Cursor(board)

    def render(self):
        def render_row(i):
            def render_space(j):
                piece = self.board.rows[i][j]
                return " ! " if self.cursor.current_pos == [i, j] else " " + piece.symbol + " "
            return ''.join(render_space(j) for j in range(8))

        print '\n'.join(render_row(i) for i in range(8))
