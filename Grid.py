from Container import Container
import numpy as np
import random


class Grid:

    def __init__(self):

        self.grid = np.empty((9, 9), dtype=object)

        for i in range(9):
            for j in range(9):
                self.grid[i, j] = Container(0)

    def __str__(self):
        return_string = ''
        for i in range(self.grid.shape[0]):
            for container in self.grid[i,:]:
                return_string += '|' + str(container)
            return_string += '|\n'
        return return_string

    def update_poss_val(self, x, y, n):
        for container in self.grid[:, x]:
            container.possible_values[n-1] = False

        for container in self.grid[y, :]:
            container.possible_values[n-1] = False

        for i in range(3):
            x_square = (x // 3) * 3 + i
            for j in range(3):
                y_square = (y // 3) * 3 + j
                self.grid[y_square, x_square].possible_values[n-1] = False

    def no_zeros(self):
        sum = 0
        for line in self.grid:
            for container in line:
                sum += (container.true_value == 0)
        return 81 - sum

    def init_solution(self):
        print(self)

        while self.no_zeros() != 17:
            x = random.randint(0, 8)
            y = random.randint(0, 8)
            if self.grid[y, x].get_true_value() == 0:
                poss_val = self.grid[y, x].possible_int_values()  # Get possible values for square
                value = random.choice(poss_val)  # Select a random value
                self.grid[y, x].set_true_value(value)  # Update true value of square
                self.update_poss_val(x, y, value)
        print(self)

if __name__ == '__main__':
    test = Grid()
    test.init_solution()
    print(test.no_zeros())
    #print(test.grid[3, 1].possible_int_values())
    #print(test)

    #print(test.grid[1, 3].possible_int_values())
    #print(test.grid[1, 3].guessed_value)

