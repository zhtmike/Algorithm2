from csv import reader
from operator import itemgetter

from tools.union_finder import UnionFinder


class Assign2(object):
    """
    Assignment 2
    """

    @staticmethod
    def read_edge_list(txt_name):
        """
        Read the first line as total number of nodes
        Read the remaining part as a dict of edge pair
        :param txt_name: (str) location of the txt
        :return: (dict) {edge 1 cost: (edge 1 node 1, edge 1 node2) ...}
        """
        edge_list = []
        node_list = set()
        with open(txt_name, 'r') as csv_file:
            total_node = int(csv_file.readline())
            remain = reader(csv_file, delimiter=' ')
            for row in remain:
                node_a, node_b, cost = map(int, row)
                edge_list.append((node_a, node_b, cost))
                node_list.add(node_a)
                node_list.add(node_b)
        # check the total number of nodes
        assert len(node_list) == total_node
        return edge_list, node_list

    def question_one(self, txt_name, num_clusters=4):
        """
        Implement a max-spacing k-clustering.
        :param txt_name: (str) location of the txt
        :param num_clusters: (int) the total number of clusters k
        :return: (int) the maximum distance between k clusters
        """

        edge_list, node_list = self.read_edge_list(txt_name)
        sorted_edge = sorted(edge_list, key=itemgetter(2))
        # insert all nodes to the union find structure
        uf = UnionFinder(max(node_list) + 1)
        count = len(node_list)  # number of cluster
        # scan all the edges until there are remains k clusters
        for node_a, node_b, cost in sorted_edge:
            if uf.find(node_a) != uf.find(node_b):
                if count == num_clusters:
                    return cost
                uf.merge(node_a, node_b)
                count -= 1
        raise IndexError


if __name__ == '__main__':
    assign2 = Assign2()
    assign2.question_one('data/assign2/_fe8d0202cd20a808db6a4d5d06be62f4_clustering1.txt')
