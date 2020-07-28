import random
import numpy as np


class Container:

    def __init__(self, value=-1):
        if value == -1:
            self.true_value = random.randint(1, 9)
        else:
            self.true_value = value

        self.possible_values = np.ones(9, dtype=bool)  # True if the corresponding index +1 is a possible value
        self.guessed_value = 0

    def __str__(self):
        return str(self.true_value)

    def possible_int_values(self):
        return_array = []
        for i, poss in enumerate(self.possible_values):
            if poss:
                return_array.append(i + 1)
        return return_array

    def set_true_value(self, n):
        self.true_value = n

    def set_guessed_value(self, n):
        self.guessed_value = n

    def get_true_value(self):
        return self.true_value

    def get_guessed_value(self):
        return self.guessed_value

    def is_possible(self, n):
        return self.possible_values[n - 1]


if __name__ == '__main__':
    test = Container(5)
    print(test)

    test = Container(0)
    print(test)

    print(test.is_possible(4))
    print(test.possible_int_values())
