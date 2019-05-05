class HumanPlayer:
    def __init__(self, color, display):
        self.color = color
        self.display = display

    def get_move(self):
        start_pos, end_pos = None, None

        while not start_pos or not end_pos:
            selected_pos = self.display.cursor.handle_input

            if selected_pos:
                if not start_pos:
                    print self.color + "'s turn. Move from where?'"
                    start_pos = selected_pos
                else:
                    print self.color + "'s turn. Move to where?'"
                    end_pos = selected_pos

            return start_pos, end_pos
