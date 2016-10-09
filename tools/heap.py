import heapq as hq


class Heap(object):
    """
    The Heap object.
    A slightly modified version of the illustration:
    https://docs.python.org/3.5/library/heapq.html
    """

    def __init__(self, pq=None):
        """
        Heapify the entries if pq is not None.
        :param pq: list of entries
        """
        self.REMOVED = '<removed-task>'
        if not pq:
            self.pq = []
            self.entry_finder = {}
        else:
            self.pq = pq
            hq.heapify(self.pq)
            self.entry_finder = {entry[1]: entry for entry in pq}

    def add_task(self, task, priority=0):
        """
        Add a new task or update the priority of an existing task
        :param task: (str) task name
        :param priority: (int) task priority
        """
        if task in self.entry_finder:
            self.remove_task(task)
        entry = [priority, task]
        self.entry_finder[task] = entry
        hq.heappush(self.pq, entry)

    def remove_task(self, task):
        """
        Mark an existing task as REMOVED.  Raise KeyError if not found.
        :param task: (str) task name
        """
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def pop_task(self):
        """
        Remove and return the lowest priority task.
        :return: (str, int) task name with lowest priority, lowest priority
        """
        while self.pq:
            priority, task = hq.heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task, priority
        raise KeyError('pop from an empty priority queue')
