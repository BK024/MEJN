from random import randrange


class Dice:
    def __init__(self):
        self.history_list = []
        self.current_value = -1

    def roll(self):
        new_value = randrange(1, 7)
        self.history_list.append(new_value)
        self.current_value = new_value
        return self.current_value

