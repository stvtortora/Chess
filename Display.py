from Cursor import Cursor

class Display:
    def __init__(self, board):
        # self.cursor = Cursor()
        self.board = board
        self.cursor = Cursor(board)

    def render(self):
        for row in self.board.rows:
            row_display = ''
            for piece in row:
                row_display += " " + piece.symbol + " "
            print row_display
