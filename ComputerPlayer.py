# -*- encoding: utf-8 -*-
import random
value_map = {
  u'♜': 500, u'♞': 350, u'♝': 350, u'♛': 1000,
  u'♚': 10000, u'♟': 100, u'♖': 500, u'♘': 350,
  u'♗': 350, u'♕': 1000, u'♔': 10000, u'♙': 100
}

class ComputerPlayer(object):
    def __init__(self, color, display):
        self.color = color
        self.display = display

    def evaluate(self, board):
        value = 0
        for row in board.rows:
            for piece in row:
                if piece.color:
                    value = value + value_map[piece.symbol] if piece.color == self.color else value - value_map[piece.symbol]
        return value


    def move_options(self, board):
        result = []
        for row in board.rows:
            for piece in row:
                if piece.color and piece.color == self.color:
                    result += [[piece.pos, end_pos] for end_pos in piece.valid_moves()]
        return result

    def get_move(self):
        self.display.render()
        print('Computer\'s turn')
        value, move = self.calculate_move(self.display.board, True, float("-inf"), float("inf"), 3)
        start_pos, end_pos = move
        return start_pos, end_pos

    def calculate_move(self, board, maximizing_player, alpha, beta, depth):
        if depth == 0:
            return self.evaluate(board), None

        best_move = None
        best_move_value = float("-inf") if maximizing_player else float("inf")
        move_options = self.move_options(board)
        random.shuffle(move_options)


        for move in move_options:
            start_pos, end_pos = move
            board_copy = board.copy()
            board_copy.move_piece(start_pos, end_pos)

            move_value = self.calculate_move(board_copy, not maximizing_player, alpha, beta, depth - 1)[0]

            if maximizing_player:
                if move_value > best_move_value:
                    best_move_value = move_value
                    best_move = move
                alpha = max(alpha, move_value)
            if not maximizing_player:
                if move_value < best_move_value:
                    best_move_value = move_value
                    best_move = move
                beta = min(beta, move_value)

            if beta < alpha:
                break

        return best_move_value, best_move
