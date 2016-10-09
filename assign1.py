from collections import defaultdict
from csv import reader
from itertools import accumulate
from math import inf

from tools.heap import Heap


class Assign1(object):
    """
    Assignment 1
    """

    @staticmethod
    def read_weight_length(txt_name):
        """
        Read the first line as the total number,
        Read the remaining part as a list of (weight, length).
        :param txt_name: (str) location of the txt
        :return: (list) list of (weight, length)
        """
        job_list = []
        with open(txt_name, 'r') as csv_file:
            total_num = int(csv_file.readline())
            remain = reader(csv_file, delimiter=' ')
            for row in remain:
                job_list.append([int(x) for x in row])
        assert total_num == len(job_list)
        return job_list

    @staticmethod
    def read_graph(txt_name):
        """
        Read the first line as total number of nodes, total number of edges
        Read the remaining part as a adjacent list of graph (node: cost)
        :param txt_name: (str) location of the txt
        :return: (dict) the adjacent list. i.e. {node1: {{node2: cost}, {node3: cost} ...} ...}
        """
        adjacent_list = defaultdict(dict)
        with open(txt_name, 'r') as csv_file:
            total_node, total_edge = map(int, csv_file.readline().split(maxsplit=1))
            remain = reader(csv_file, delimiter=' ')
            for row in remain:
                adjacent_list[row[0]][row[1]] = int(row[2])
                adjacent_list[row[1]][row[0]] = int(row[2])
        # check the total number of nodes and edges
        assert len(adjacent_list) == total_node
        assert sum([len(sub_dict) for sub_dict in adjacent_list.values()]) / 2 == total_edge
        return adjacent_list

    def question_one(self, txt_name):
        """
        Minimize the completion time by sorting the job according to weight - length
        :param txt_name: (str) location of the txt
        :return: total sum of weighted completion time
        """
        job_list = self.read_weight_length(txt_name)
        # Sorting the job by (first, weight - length; second, weight) reversely
        sorted_list = sorted(job_list, key=lambda info: (info[0] - info[1], info[0]), reverse=True)
        # Accumulate the completion time
        completion_time = list(accumulate([item[1] for item in sorted_list]))
        # Compute the weighted completion time
        weighted_completion_time = [sorted_list[i][0] * completion_time[i] for i in range(len(sorted_list))]
        return sum(weighted_completion_time)

    def question_two(self, txt_name):
        """
        Minimize the completion time by sorting the job according to weight / length
        :param txt_name: (str) location of the txt
        :return: total sum of weighted completion time
        """
        job_list = self.read_weight_length(txt_name)
        # Sorting the job by (first, weight - length; second, weight) reversely
        sorted_list = sorted(job_list, key=lambda info: info[0] / info[1], reverse=True)
        # Accumulate the completion time
        completion_time = list(accumulate([item[1] for item in sorted_list]))
        # Compute the weighted completion time
        weighted_completion_time = [sorted_list[i][0] * completion_time[i] for i in range(len(sorted_list))]
        return sum(weighted_completion_time)

    def question_three(self, txt_name):
        """
        Run Prism's minimum spanning tree algorithm and calculate the total cost of the minimum spanning tree
        :param txt_name: (str) location of the txt
        :return: (int) the total cost
        """
        adj_list = self.read_graph(txt_name)
        # Set all the nodes to be non-explored
        check_list = {node: False for node in adj_list}

        # Pick up a random node and set up the heap list
        initial_node = next(iter(adj_list.keys()))
        check_list[initial_node] = True
        pq = [[adj_list[initial_node].get(node, inf), node] for node in adj_list if node is not initial_node]
        heap = Heap(pq)

        # iterate the remaining node until all nodes are explored.
        total_cost = 0
        while heap.pq:
            nearest_node, cost = heap.pop_task()
            total_cost += cost
            check_list[nearest_node] = True
            for node, value in adj_list[nearest_node].items():
                if not check_list[node]:
                    heap.add_task(node, min(heap.entry_finder[node][0], value))

        return total_cost


if __name__ == '__main__':
    assign1 = Assign1()
    weight_job_path = 'data/assign1/_642c2ce8f3abe387bdff636d708cdb26_jobs.txt'
    graph_path = 'data/assign1/_d4f3531eac1d289525141e95a2fea52f_edges.txt'
    print(assign1.question_one(weight_job_path))
    print(assign1.question_two(weight_job_path))
    print(assign1.question_three(graph_path))
