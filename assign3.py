from csv import reader

import numba as nb
import numpy as np


class Assign3(object):
    """
    Assignment 3
    """

    def __init__(self):
        """
        Define several variables
        """
        self.knapsack_size = 0
        self.item_list = []
        self.number_of_items = 0

    def read_value_weight(self, txt_name):
        """
        Read the first line as the knapsack size, number of items,
        Read the remaining part as a list of (value, weight).
        :param txt_name: (str) location ofs the txt
        :return: (list) list of (value, weight)
        """
        self.item_list = []
        with open(txt_name, 'r') as csv_file:
            self.knapsack_size, self.number_of_items = map(int, csv_file.readline().split(maxsplit=1))
            remain = reader(csv_file, delimiter=' ')
            for row in remain:
                value, weight = map(int, row)
                self.item_list.append((value, weight))
        assert self.number_of_items == len(self.item_list)

    def compute_optimal(self):
        """
        Compute the value of the optimal solution by Dynamic programming
        Wrapper of _compute_optimal
        :return: (int) the value of optimal solution
        """
        items = np.array(self.item_list, dtype=np.uint)
        return self._compute_optimal(items, self.number_of_items, self.knapsack_size)

    @staticmethod
    @nb.jit(nb.uint(nb.uint[:, :], nb.uint, nb.uint), nopython=True, cache=True)
    def _compute_optimal(items, n, W):
        """
        Compute the value of the optimal solution by Dynamic programming
        :param items: (np.array) item list
        :param n: (int) number of items
        :param W: (int) knapsack size
        :return: (int) the value of optimal solution
        """
        ma = np.zeros((n + 1, W + 1), dtype=np.uint)
        value, weight = nb.uint(0), nb.uint(0)
        for i in range(1, n + 1):
            for x in range(W + 1):
                value, weight = items[i - 1]
                if weight > x:
                    ma[i, x] = ma[i - 1, x]
                else:
                    ma[i, x] = max(ma[i - 1, x], ma[i - 1, x - weight] + value)
        return ma[n, W]

    def question(self, txt_name):
        """
        Calculate the optimal value under the constraint that the total weight is less than knapsack size
        :param txt_name: (str) location of the txt
        :return: (int) the value of optimal solution
        """
        self.read_value_weight(txt_name)
        return self.compute_optimal()


if __name__ == '__main__':
    assign3 = Assign3()
    print(assign3.question('data/assign3/_6dfda29c18c77fd14511ba8964c2e265_knapsack1.txt'))
    print(assign3.question('data/assign3/_6dfda29c18c77fd14511ba8964c2e265_knapsack_big.txt'))
