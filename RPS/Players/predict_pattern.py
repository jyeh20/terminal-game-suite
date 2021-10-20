import random

class PredictPatterns:
    def __init__ (self, name):
        self.wins = 0
        self.name = name
        self.move = ""
        self.input = ["ROCK", "PAPER", "SCISSORS"]

    def get_input(self, opp_info):
        dist = opp_info[0]
        rock_chance, paper_chance, scissors_chance = dist["ROCK"], dist["PAPER"], dist["SCISSORS"]
        total = rock_chance + paper_chance + scissors_chance
        rock_chance = int((rock_chance/total) * 100)
        paper_chance = int((paper_chance/total) * 100) + rock_chance
        chance = random.randint(0, 100)
        if chance < rock_chance:
            self.move = "PAPER"
        if rock_chance <= chance < paper_chance:
            self.move = "SCISSORS"
        else:
            self.move = "ROCK"
        return self.move

    def __str__(self):
        return f"[ {self.move} ]"