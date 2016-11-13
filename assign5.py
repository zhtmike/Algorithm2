import itertools as it
from csv import reader

import numpy as np
from numpy.linalg import norm


class Assign5(object):
    """
    Assignment 5
    """

    def __init__(self):
        self.size = 0
        self.cities = None
        self.pair_dist = None

    @staticmethod
    def read_node_list(txt_name: str) -> list:
        """
        Read the first line as total number of cities
        Read the remaining part as a list of x-cor, y-cor
        :param txt_name: location of the txt
        :return: city list
        """
        city_list = []
        with open(txt_name, 'r') as csv_file:
            total_city = int(csv_file.readline())
            remain = reader(csv_file, delimiter=' ')
            for x, y in remain:
                city_list.append((float(x), float(y)))
        # check the total number of nodes
        assert len(city_list) == total_city
        return len(city_list), np.array(city_list)

    @staticmethod
    def powerset(iterable: iter) -> iter:
        """
        powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
        https://docs.python.org/3/library/itertools.html#itertools.product
        :param iterable:
        :return: iterable set
        """
        s = list(iterable)
        return it.chain.from_iterable(it.combinations(s, r) for r in range(len(s) + 1))

    def dist_pair(self) -> dict:
        """
        Return the each pairs distance
        :return: (dict) (city 1, city 2): Euclidean Distance
        """
        pairs = it.product(range(self.size), range(self.size))
        return {(x, y): norm(self.cities[x] - self.cities[y]) for x, y in pairs}

    def shortest_path(self):
        subsets = list(self.powerset(range(1, self.size)))
        subsets = dict(zip(subsets, range(2 ** self.size)))
        values = np.zeros((2 ** (self.size - 1), self.size), dtype=np.float32)
        values[:, :] = np.infty
        values[subsets[()], 0] = 0
        for m in range(1, self.size):
            print("{0}'s column...".format(m))
            for s in it.combinations(range(1, self.size), m):
                for j in s:
                    dump = tuple(i for i in s if i != j)
                    values[subsets[s], j] = min(
                        [values[subsets[dump], k] + self.pair_dist[(j, k)] for k in range(self.size) if k != j])
        print(values)
        return min([values[subsets[tuple(range(1, self.size))], j] + self.pair_dist[(j, 0)] for j in
                    range(1, self.size)])

    def question(self, txt: str) -> int:
        """
        Using dynamic programming to solve the travel's man problem
        :param txt:
        :return:
        """
        self.size, self.cities = self.read_node_list(txt)
        self.pair_dist = self.dist_pair()
        ans = self.shortest_path()
        return int(ans)


if __name__ == '__main__':
    assign5 = Assign5()
    print(assign5.question('data/assign5/_f702b2a7b43c0d64707f7ab1b4394754_tsp.txt'))
