import random

class PickLast:

    def __init__ (self, name):
        self.wins = 0
        self.name = name
        self.move = ""

    def get_input(self, opp_info):
        self.move = opp_info[1]
        if self.move == '':
            moves = ["ROCK", "PAPER", "SCISSORS"]
            self.move = moves[random.randint(0, len(moves) - 1)]
        return self.move

    def __str__(self):
        return f"[ {self.move} ]"