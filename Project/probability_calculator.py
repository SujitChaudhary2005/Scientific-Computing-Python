import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls_drawn):
        if num_balls_drawn >= len(self.contents):
            drawn_balls = self.contents[:]
            self.contents.clear()
            return drawn_balls

        drawn_balls = random.sample(self.contents, num_balls_drawn)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        experiment_hat = copy.deepcopy(hat)
        drawn = experiment_hat.draw(num_balls_drawn)
        drawn_counts = {}

        for ball in drawn:
            drawn_counts[ball] = drawn_counts.get(ball, 0) + 1

        success = True
        for ball_color, required_count in expected_balls.items():
            if drawn_counts.get(ball_color, 0) < required_count:
                success = False
                break

        if success:
            success_count += 1

    return success_count / num_experiments

# Example run
hat = Hat(black=6, red=4, green=3)
probability = experiment(
    hat=hat,
    expected_balls={'red': 2, 'green': 1},
    num_balls_drawn=5,
    num_experiments=2000
)
print(f"Estimated Probability: {probability:.4f}")