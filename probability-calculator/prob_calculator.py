import random


class Hat:

    def __init__(self, **colours):
        self.contents = sum([[color] * amount for color, amount in colours.items()], [])
        self.copy = self.contents[:]

    def draw(self, number):
        self.contents = self.copy[:]
        if number >= len(self.contents):
            return self.contents
        choices = random.choices(self.contents, k=number)
        for item in choices:
            if item in self.contents:
                self.contents.remove(item)
        return choices


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    expected_balls = sum([[color] * amount for color, amount in expected_balls.items()], [])
    i = 0
    while i < num_experiments:
        drawed_balls = hat.draw(num_balls_drawn) 
        if all(item in drawed_balls for item in expected_balls):
            m += 1
        i += 1
    return m / num_experiments