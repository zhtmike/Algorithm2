from csv import reader
from operator import itemgetter

from src.union_finder import UnionFinder


class Assign2(object):
    """
    Assignment 2
    """

    @staticmethod
    def read_edge_list(txt_name):
        """
        Read the first line as total number of nodes
        Read the remaining part as a list of edges
        :param txt_name: (str) location of the txt
        :return: (list, list) edge list, node list
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

    @staticmethod
    def read_node_list(txt_name):
        """
        Read the first line as total number of nodes, length of the bits
        Read the remaining part as a list of nodes, with each node's location is represented a binary string
        :param txt_name: (str) location of the txt
        :return: (list) nodes list
        """
        node_list = []
        with open(txt_name, 'r') as csv_file:
            total_node, num_bits = map(int, csv_file.readline().split())
            remain = reader(csv_file, delimiter=' ')
            for row in remain:
                bits = ''.join(row)
                assert len(bits) == num_bits, 'len = ' + str(len(row))
                node_list.append(bits)
        # check the total number of nodes
        # assert len(node_list) == total_node
        return node_list

    @staticmethod
    def hamming(str_1, str_2):
        """
        compute the string 1 and string 2's hamming distance
        :param str_1: (str) string 1
        :param str_2: (str) string 2
        :return: (int) hamming distance
        """
        # assert len(str_1) == len(str_2), "lengths of two strings are unequal."
        diff_list = [1 for i in range(len(str_1)) if str_1[i] != str_2[i]]
        return sum(diff_list)

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

    def question_two(self, txt_name, N=3):
        node_list = self.read_node_list(txt_name)
        uf = UnionFinder(len(node_list))
        node_dict = {}
        for i in range(len(node_list)):
            j = node_dict.get(node_list[i], -1)
            if j == -1:
                node_dict[node_list[i]] = i
            else:
                uf.merge(i, j)

        # for n in range(1, N):
        #     for i in range(len(node_list)):
        #         for j in range(len(node_list)):
        #             if self.hamming(node_list[i], node_list[j]) == n:
        #                 uf.merge(i, j)

        unions = set()
        for i in uf.union:
            unions.add(uf.find(i))
        return len(unions)

if __name__ == '__main__':
    assign2 = Assign2()
    # print(assign2.question_one('data/assign2/_fe8d0202cd20a808db6a4d5d06be62f4_clustering1.txt'))
    print(assign2.question_two('data/assign2/_fe8d0202cd20a808db6a4d5d06be62f4_clustering_big.txt'))
    # print(assign2.question_two('data/assign2/test_case/q22.txt'))
