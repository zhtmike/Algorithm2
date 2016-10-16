class UnionFinder(object):
    """
    Naive implementation of the union find
    Each node should be mapped to the index of the union list
    """

    def __init__(self, num: int):
        """
        Initiate the union list and corresponding counter
        :param num: (int) number of nodes
        """
        self.union = [i for i in range(0, num)]
        self.union_count = [1] * num  # the number of nodes in each union is stored in the leader index

    def find(self, node: int):
        """
        Find the leader of corresponding node
        :param node: (int) index of the node
        :return: (int) leader's index of the node
        """
        return self.union[node]

    def merge(self, node_1: int, node_2: int):
        """
        Merge the unions containing node 1 and node 2
        :param node_1: (int) index of the node
        :param node_2: (int) index of the node
        """
        # compare union containing node 1 and node 2
        leader_1, leader_2 = self.union[node_1], self.union[node_2]
        if self.union_count[leader_1] >= self.union_count[leader_2]:
            leader, follower = leader_1, leader_2
        else:
            leader, follower = leader_2, leader_1
        # scans all nodes and merge the follower's union to leader's union
        for ind in range(len(self.union)):
            if self.union[ind] == follower:
                self.union[ind] = leader

        self.union_count[leader] += self.union_count[follower]
