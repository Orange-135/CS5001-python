import random

MAX_NUMBER = 6
MIN_NUMBER = 1


class Die:
    def __init__(self):
        self.roll()

    def roll(self):
        self.current_value = random.randint(MIN_NUMBER, MAX_NUMBER)

    def __str__(self):
        return str(self.current_value)
