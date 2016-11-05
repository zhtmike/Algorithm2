import numba as nb
import numpy as np

from tools.read_graph import read_directed_graph


class Assign4(object):
    """
    Assignment 4
    """
    INF = np.iinfo(np.int32).max  # The value represents infinity

    def __init__(self):
        """
        Graphs is a list of adjacent list
        """
        self.graphs = []

    def set_boundary(self, graph: dict, n: int) -> np.ndarray:
        """
        Set the boundary case of the matrix
        :param graph: adjacent list
        :param n: number of nodes
        :return: matrix represents the min. path
        """
        ma = np.zeros((n + 1, n + 1, 2), dtype=np.int32)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i != j:
                    ma[i, j, 0] = graph[i].get(j, self.INF)
        return ma

    @staticmethod
    @nb.jit(nb.int32[:, :](nb.int32[:, :, :], nb.uint32), nopython=True, cache=True)
    def compute_minimum(ma: np.ndarray, n: int) -> np.ndarray:
        """
        Compute the shortest path between each pair of nodes
        :param ma: adjacent list
        :param n: number of nodes
        :return: the shortest path between nodes
        """
        for k in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    ma[i, j, k % 2] = min(ma[i, j, (k - 1) % 2], ma[i, k, (k - 1) % 2] + ma[k, j, (k - 1) % 2])
        return ma[:, :, n % 2]

    def FW_algorithm(self, graph: np.ndarray, n: int) -> int:
        """
        Compute the shortest of the shortest path according to Floyd-Warshall Algorithm
        :param graph: adjacent list
        :param n: number of nodes
        :return: the minimum distance though all nodes
        """
        ma = self.set_boundary(graph, n)
        val = self.compute_minimum(ma, n)  # type: np.ndarray
        if np.any(val.diagonal() < 0):
            return np.nan
        else:
            return val.min()

    def question(self, files: list) -> list:
        """
        Compute the shortest distance for among all nodes in a adjacent list
        :param files: lift of all text files
        :return: shortest distance or nan if there exists negative cycles
        """
        ans = []
        self.graphs = [read_directed_graph(file) for file in files]
        for graph in self.graphs:
            n, m, array = graph
            ans.append(self.FW_algorithm(array, n))
        return ans


if __name__ == '__main__':
    paths = [
        'data/assign4/_6ff856efca965e8774eb18584754fd65_g1.txt',
        'data/assign4/_6ff856efca965e8774eb18584754fd65_g2.txt',
        'data/assign4/_6ff856efca965e8774eb18584754fd65_g3.txt'
    ]
    assign4 = Assign4()
    print(assign4.question(paths))
