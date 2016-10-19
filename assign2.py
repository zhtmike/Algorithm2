import itertools as iter
from csv import reader
from ctypes import create_unicode_buffer
from operator import itemgetter

from cython_module.union_find import UnionFind


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
        :return: (str) nodes list
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
        assert len(node_list) == total_node
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
        uf = UnionFind(max(node_list) + 1)
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
        """
        Implement a max-spacing k-clustering with minimum space equals to N
        :param txt_name: (str) location of the txt
        :param N: (int) the min-spacing
        :return: (int) number of clusters
        """
        node_list = self.read_node_list(txt_name)
        uf = UnionFind(len(node_list))
        node_dict = {}
        # scan the list and merge the node with same location into same union
        for i in range(len(node_list)):
            j = node_dict.get(node_list[i], -1)
            if j == -1:
                node_dict[node_list[i]] = i
            else:
                uf.merge(i, j)

        bit_length = len(node_list[0])

        # combine the all possible cases into a single list
        comb = [list(iter.combinations(range(bit_length), n)) for n in range(1, N)]
        comb = list(iter.chain(*comb))

        # if the distance is less than N, then merge into same union
        reverse = {'0': '1', '1': '0'}
        for i in range(len(node_list)):
            for case in comb:
                dump = create_unicode_buffer(node_list[i][:])
                for j in case:
                    dump[j] = reverse[dump[j]]
                ind = node_dict.get(dump.value, -1)
                if ind != -1:
                    uf.merge(i, ind)
        # list all unions
        unions = uf.print_all()
        return len(unions)


if __name__ == '__main__':
    assign2 = Assign2()
    print(assign2.question_one('data/assign2/_fe8d0202cd20a808db6a4d5d06be62f4_clustering1.txt'))
    print(assign2.question_two('data/assign2/_fe8d0202cd20a808db6a4d5d06be62f4_clustering_big.txt'))
