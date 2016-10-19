import array
from cpython cimport array

cdef class UnionFind(object):
    """
    Naive implementation of the union find
    Each node should be mapped to the index of the union list
    """
    cdef int[:] union
    cdef int[:] union_count

    def __init__(self, int num):
        """
        Initiate the union list and corresponding counter
        :param num: (int) number of nodes
        """
        self.union = array.array('i', [i for i in range(0, num)])
        self.union_count = array.array('i', [1] * num)  # the number of nodes in each union is stored in the leader index

    def find(self, int node):
        """
        Find the leader of corresponding node
        :param node: (int) index of the node
        :return: (int) leader's index of the node
        """
        return self.union[node]

    cdef _merge(self, int node_1, int node_2):
        """
        Merge the unions containing node 1 and node 2
        :param node_1: (int) index of the node
        :param node_2: (int) index of the node
        """
        cdef int leader_1, leader_2, leader, follower
        if node_1 == node_2 or self.union[node_1] == self.union[node_2]:
            return
        # compare union containing node 1 and node 2
        leader_1, leader_2 = self.union[node_1], self.union[node_2]
        if self.union_count[leader_1] >= self.union_count[leader_2]:
            leader, follower = leader_1, leader_2
        else:
            leader, follower = leader_2, leader_1
        # scans all nodes and merge the follower's union to leader's union
        cdef int ind
        cdef int union_len = len(self.union)
        for ind in range(union_len):
            if self.union[ind] == follower:
                self.union[ind] = leader

        self.union_count[leader] += self.union_count[follower]

    def merge(self, int node_1, int node_2):
        """
        Python wrapper of _merge
        :param node_1: node_1: (int) index of the node
        :param node_2: node_1: (int) index of the node
        """

        self._merge(node_1, node_2)

    def print_all(self):
        """
        print all unions
        :return: (set) unions
        """
        cdef int i
        leaders = set()
        for i in self.union:
            leaders.add(self.find(i))
        return leaders
