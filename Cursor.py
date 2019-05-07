key_map = {
  " ": "space",
  "h": "left",
  "j": "down",
  "k": "up",
  "l": "right",
  "w": "up",
  "a": "left",
  "s": "down",
  "d": "right",
  "\t": "tab",
  "\r": "return",
  "\n": "newline",
  "\e": "escape",
  "\e[A": "up",
  "\e[B": "down",
  "\e[C": "right",
  "\e[D": "left",
  "\177": "backspace",
  "\004": "delete",
  "\u0003": "ctrl_c",
}

moves = {
  "left": [0, -1],
  "right": [0, 1],
  "up": [-1, 0],
  "down": [1, 0]
}

import os

if os.name == 'nt':
    import msvcrt
else:
    import getch

class Cursor:
    def __init__(self, board):
        self.current_pos = [0, 0]
        self.board = board

    def handle_input(self):
        key_press = input() if os.name == 'nt' else getch.getch()

        if key_press in key_map:
            action = key_map[key_press]
            if action in moves.keys():
                self.update_current_pos(moves[action])
                return None
            elif action == "space" or action == "enter":
                return self.current_pos
            else:
                return None
        return None

    def update_current_pos(self, shift):
        new_pos = [self.current_pos[0] + shift[0], self.current_pos[1] + shift[1]]
        if self.board.on_board(new_pos):
            self.current_pos = new_pos

    def user_input(self):
        i = msvrt.getch() if os.name == 'nt' else getch.getch()
        return i
