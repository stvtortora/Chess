KEYMAP = {
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

MOVES = {
  "left": [0, -1],
  "right": [0, 1],
  "up": [-1, 0],
  "down": [1, 0]
}

class Cursor:
    def __init__(self, board):
        self.current_pos = [0, 0]
        self.board = board

    def handle_input(self):
        input = KEYMAP[self.user_input()]
        print input
        if input in MOVES.keys():
            self.update_current_pos(MOVES[input])
            return None
        elif input == "space":
            print("whore")
            return self.current_pos

    def update_current_pos(self, shift):
        new_pos = [self.current_pos[0] + shift[0], self.current_pos[1] + shift[1]]
        if self.board.valid_pos(new_pos):
            self.current_pos = new_pos

    def user_input(self):
        try:
            input = raw_input()
        except:
            "Invalid key press"
        return input
