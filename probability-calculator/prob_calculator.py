import random
import copy

class Hat:

    def __init__(self, **colours):
        self.contents = sum([[color] * amount for color, amount in colours.items()], [])
        self.copy = self.contents.copy()

    def draw(self, number):
        self.contents = self.copy.copy()
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
        checked, is_matching = [], []
        for ball in expected_balls:
            if ball not in checked:
                if expected_balls.count(ball) <= drawed_balls.count(ball):
                    is_matching.append(1)
                else:
                    is_matching.append(0)
                checked.append(ball)
        if all(is_matching):
            m += 1
        i += 1
    return m / num_experiments