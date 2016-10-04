import heapq as hq


class Heap(object):
    def __init__(self, arg=None):
        if not arg:
            arg = []
        # The arg should not be mutated
        self.heap_list = arg[:]
        hq.heapify(self.heap_list)


if __name__ == '__main__':
    tmp = [2, 3, 4]
    hp = Heap(tmp)
