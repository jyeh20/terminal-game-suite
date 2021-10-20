from Board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = ""

    def player_turn(self, value):
        col = int(input("Which column would you like to add to? "))
        if col < 0 or col >= len(self.board.board[0]):
            print("Invalid column")
            self.player_turn(value)
        update = self.board.update_space(col, value)
        if not update:
            print("Invalid column")
            self.player_turn(value)
        return


    def play(self):
        while not self.board.is_win():
            self.current_player = self.get_current_player()
            print(str(self.board))
            print("Player " + self.current_player + " turn:")
            self.player_turn(self.current_player)
            if self.board.no_valid_moves():
                break
        if self.board.is_win():
            print(str(self.board))
            print("*" * 49)
            print("******************Player " + self.current_player + " WINS******************")
            print("*" * 49)
        if self.board.no_valid_moves():
            print(str(self.board))
            print("*" * 46)
            print("******************IT'S A TIE******************")
            print("*" * 46)

    def get_current_player(self):
        if self.current_player == "" or self.current_player == "X":
            return "O"
        return "X"

game = Game()
game.play()