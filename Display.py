from Cursor import Cursor

class Display:
    def __init__(self, board):
        self.board = board
        self.cursor = Cursor(board)

    def render(self):
        for i in range(8):
            row_display = ''
            for j in range(8):
                if self.cursor.current_pos == [i, j]:
                    row_display += " ! "
                else:
                    piece = self.board.rows[i][j]
                    row_display += " " + piece.symbol + " "
            print row_display
