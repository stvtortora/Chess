import os
from Cursor import Cursor
from colored import fg, bg, attr

class Display(object):
    def __init__(self, board):
        self.board = board
        self.cursor = Cursor(board)

    def isEven(self, n):
        return n % 2 == 0

    def both_odd(self, i, j):
        return not self.isEven(i) and not self.isEven(j)

    def both_even(self, i, j):
        return self.isEven(i) and self.isEven(j)

    def render(self):
        def render_row(i):
            def render_square(j):
                piece = self.board.rows[i][j]
                bg_color = 'green' if self.both_odd(i, j) or self.both_even(i, j) else 'blue'
                if self.cursor.current_pos == [i, j]:
                    bg_color = 'yellow'
                return f'%s%s {piece.symbol} %s' % (fg('white'), bg(bg_color), attr('reset'))
            return ''.join(render_square(j) for j in range(8))

        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n'.join(render_row(i) for i in range(8)))
