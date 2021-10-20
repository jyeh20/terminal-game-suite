import os, getpass

class Player:

    def __init__ (self, name):
        self.wins = 0
        self.name = name
        self.move = ""
        self.valid_input = ["rock", "paper", "scissors", "r", "p", "s"]

    def get_input(self, opp_info):
        string = f"{self.name}: choose [ROCK, PAPER, SCISSORS] "
        p = getpass.getpass(string)
        p = p.lower()
        if p in self.valid_input:
            char = p[0]
            if char == 'r':
                self.update_move("ROCK")
                return self.move
            if char == 'p':
                self.update_move("PAPER")
                return self.move
            if char == 's':
                self.update_move("SCISSORS")
                return self.move
        self.getInput()

    def update_move (self, move):
        self.move = move
        os.system('cls')

    def __str__(self):
        return f"[ {self.move} ]"