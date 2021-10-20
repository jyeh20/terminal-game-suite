import random

class RandomAgent:

    def __init__ (self, name):
        self.wins = 0
        self.name = name
        self.move = ""
        self.valid_moves = ["ROCK", "PAPER", "SCISSORS"]

    def get_input(self, opp_info):
        move_index = random.randint(0, len(self.valid_moves)-1)
        self.move = self.valid_moves[move_index]
        return self.move

    def __str__(self):
        return f"[ {self.move} ]"