class Space:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.value = " "

    def update_value(self, value):
        self.value = value

    def equals(self, other):
        return self.value == other.value