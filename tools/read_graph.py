from collections import defaultdict
from csv import reader


def read_directed_graph(txt_name: str) -> tuple:
    """
    Read the first line as total number of nodes, total number of edges
    Read the remaining part as a adjacent list of graph
    :param txt_name: location of the txt
    :return: number of node, number of edge, the adjacent list. i.e. {node1: {{node2: cost}, {node3: cost} ...} ...}
    """
    adjacent_list = defaultdict(dict)
    nodes = set()
    with open(txt_name, 'r') as csv_file:
        total_node, total_edge = map(int, csv_file.readline().split(maxsplit=1))
        remain = reader(csv_file, delimiter=' ')
        for row in remain:
            node1, node2, cost = map(int, row)
            nodes.add(node1)
            nodes.add(node2)
            adjacent_list[node1][node2] = cost
    # check the total number of nodes and edges
    assert len(nodes) == total_node, '{0} != {1}'.format(nodes, total_node)
    sum_edges = sum([len(sub_dict) for sub_dict in adjacent_list.values()])
    assert sum_edges == total_edge, '{0} != {1}'.format(sum_edges, total_edge)
    return total_node, total_edge, adjacent_list


def read_undirected_graph(txt_name: str) -> tuple:
    """
    Read the first line as total number of nodes, total number of edges
    Read the remaining part as a adjacent list of graph
    :param txt_name: location of the txt
    :return: number of node, number of edge, the adjacent list. i.e. {node1: {{node2: cost}, {node3: cost} ...} ...}
    """
    adjacent_list = defaultdict(dict)
    with open(txt_name, 'r') as csv_file:
        total_node, total_edge = map(int, csv_file.readline().split(maxsplit=1))
        remain = reader(csv_file, delimiter=' ')
        for row in remain:
            node1, node2, cost = map(int, row)
            adjacent_list[node1][node2] = cost
            adjacent_list[node2][node1] = cost
    # check the total number of nodes and edges
    assert len(adjacent_list) == total_node, '{0} != {1}'.format(len(adjacent_list), total_node)
    # computer the total edges
    sum_edges = sum([len(sub_dict) for sub_dict in adjacent_list.values()]) / 2
    assert sum_edges == total_edge, '{0} != {1}'.format(sum_edges, total_edge)
    return total_node, total_edge, adjacent_list
