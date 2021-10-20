import os, sys, math

from Players.player import Player
from Players.random import RandomAgent
from Players.rock import Rock
from Players.predict_pattern import PredictPatterns
from Players.pick_last import PickLast

class RPS:
    def __init__(self, agent_1, agent_2):
        self.p1 = self.construct_agent(agent_1, 1)
        self.p2 = self.construct_agent(agent_2, 2)
        self.win_dict = {
            "ROCK" : "SCISSORS",
            "PAPER" : "ROCK",
            "SCISSORS" : "PAPER"
        }
        self.total_games = 0
        self.p1_dist = {"ROCK": 0, "PAPER": 0, "SCISSORS": 0}
        self.p2_dist = {"ROCK": 0, "PAPER": 0, "SCISSORS": 0}

    def get_win(self):
        if self.win_dict[self.p1.move] == self.p2.move:
            self.p1.wins += 1
            return f"{self.p1.name} WINS"
        elif self.p1.move == self.p2.move:
            return "TIE"
        self.p2.wins += 1
        return f"{self.p2.name} WINS"

    def construct_agent(self, agent, id):
        agents = {
            "PLAYER" : Player(f"{agent} {str(id)}"),
            "RANDOMAGENT" : RandomAgent(f"Random Agent {str(id)}"),
            "ROCK" : Rock(f"Rock {str(id)}"),
            "PREDICT" : PredictPatterns(f"Predictor {str(id)}"),
            "PICKLAST" : PickLast(f"Pick Last {str(id)}")
        }
        return agents[agent.upper()]

    def play(self):
        self.p1_prev = self.p1.move
        self.p2_prev = self.p2.move
        p1_input_tup = (self.p2_dist, self.p2.move)
        p2_input_tup = (self.p1_dist, self.p1.move)
        self.p1_dist[self.p1.get_input(p1_input_tup)] += 1
        self.p2_dist[self.p2.get_input(p2_input_tup)] += 1
        self.game_report()
        print(f"CURRENT SCORE: {self.get_scores()}")

    def game_report (self):
        print(f"{self.p1.name.upper()} CHOSE: {str(self.p1)}")
        print(f"{self.p2.name.upper()} CHOSE: {str(self.p2)}")
        print("GAME RESULT:")
        self.get_win()
        print(self.get_win())
        self.total_games += 1
        print(f"TOTAL GAMES PLAYES: {self.total_games}")
        agent_1_string = "#" * int((self.p1.wins/self.total_games) * 20)
        agent_2_string = "#" * int((self.p2.wins/self.total_games) * 20)
        print(f"{agent_1_string}")
        print(f"{agent_2_string}")

    def get_scores (self):
        total = 1 if (self.p1.wins + self.p2.wins) <= 0 else self.p1.wins + self.p2.wins
        p1_wr = (self.p1.wins/total * 100)
        p2_wr = (self.p2.wins/total * 100)
        if (p1_wr > p2_wr):
            p1_wr = math.ceil(p1_wr)
            p2_wr = math.floor(p2_wr)
        else:
            p1_wr = math.floor(p1_wr)
            p2_wr = math.ceil(p2_wr)
        score_report = f"[{self.p1.name.upper()} : {str(self.p1.wins)}, {str(p1_wr)}% {self.p2.name.upper()} : {str(self.p2.wins)}, {str(p2_wr)}% ]"
        return score_report

    def play_again(self):
        play_again = input("Play again? Y/N ").upper()
        if play_again[0] == "Y":
            os.system('cls')
            return True
        if play_again[0] == "N":
            os.system('cls')
            return False
        self.play_again()

if len(sys.argv) == 3:
    os.system('cls')
    game = RPS(sys.argv[1], sys.argv[2])
    game.play()
    i = 0
    while (i < 10000):
        os.system('cls')
        game.play()
        i += 1

    print(f"FINAL SCORE: {game.get_scores()}")
else:
    print("Usage: RPS <agent_1> <agent_2>\nAgent options: [Player, RandomAgent, Rock, PickLast, Predict]")