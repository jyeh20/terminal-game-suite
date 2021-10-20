from Space import Space
import re

class Board:
    def __init__(self):
        ROWS = 6
        COLS = 7
        self.board = []
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(Space(row, col))

    def update_space(self, col, value):
        row = self.get_next_space(col)
        if row == None:
            return False
        self.board[row][col].value = value
        return True

    def get_next_space(self, col):
        row = len(self.board) - 1
        while row >= 0:
            if self.board[row][col].value == " ":
                return row
            row -= 1
        if row < 0:
            return None

    def get_rows_as_strings(self):
        return_array = []
        for row in self.board:
            string = ""
            for space in row:
                string += space.value
            return_array.append(string)
        return return_array

    def get_cols_as_strings(self):
        return_array = []
        for col in range(7):
            col_string = ""
            for row in self.board:
                col_string += row[col].value
            return_array.append(col_string)
        return return_array

    def get_diags_as_strings(self):
        return_array = []
        row = 0
        while row < len(self.board):
            if row == 0:
                for col in range(7):
                    if col <= 3:
                        c = col
                        return_array.append(self.get_diags_in_direction(c, True))
                    if col >= 3:
                        c = col
                        return_array.append(self.get_diags_in_direction(c, False))
            if row > 0 and row <= 2:
                r = row
                return_array.append(self.get_diags_on_edge(r, 0, True, True))
                return_array.append(self.get_diags_on_edge(r, len(self.board[r])-1, False, True))
            if row > 2 and row < len(self.board) - 1:
                r = row
                return_array.append(self.get_diags_on_edge(r, 0, True, False))
                return_array.append(self.get_diags_on_edge(r, len(self.board[r])-1, False, False))
            row += 1
        return(return_array)


    def __str__(self):
        return_string = ""
        for row in self.board:
            for space in row:
                return_string += "[" + space.value + "]"
            return_string += "\n"
        return_string += " 0  1  2  3  4  5  6"
        return return_string

    def get_diags_on_edge(self, row, col, x_direction, y_direction):
        diag = ""
        while (y_direction and row < len(self.board)) or (not y_direction and row >= 0):
            diag += self.board[row][col].value
            col += 1 if x_direction else -1
            row += 1 if y_direction else -1
        return diag

    def get_diags_in_direction(self, col, direction):
        diag = ""
        for row in self.board:
            diag += row[col].value
            if direction:
                col += 1
            else:
                col -= 1
            if col >= len(row) or col < 0:
                break
        return diag

    def get_board_as_strings(self):
        strings = []
        for string in self.get_rows_as_strings():
            strings.append(string)
        for string in self.get_cols_as_strings():
            strings.append(string)
        for string in self.get_diags_as_strings():
            strings.append(string)
        return strings

    def get_winner(self):
        for string in self.get_board_as_strings():
            if re.search("XXXX", string.upper()):
                return "X"
            if re.search("OOOO", string.upper()):
                return "O"

    def no_valid_moves(self):
        for row in self.board:
            for col in row:
                if col.value == " ":
                    print(col.value)
                    return False
        return True

    def is_win(self):
        return self.get_winner()