class Rock:

    def __init__ (self, name):
        self.wins = 0
        self.name = name
        self.move = ""

    def get_input(self, opp_info):
        self.move = "ROCK"
        return self.move

    def __str__(self):
        return f"[ {self.move} ]"