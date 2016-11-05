from unittest import TestCase

from tools.heap import Heap


class TestHeap(TestCase):
    def setUp(self):
        self.heap = Heap([[5, 1], [6, 3]])

    def tearDown(self):
        self.heap = None

    def test_add_task(self):
        self.heap.add_task(2, 1)
        self.assertDictEqual({1: [5, 1], 2: [1, 2], 3: [6, 3]}, self.heap.entry_finder)
        self.assertListEqual([1, 2], self.heap.pq[0])

    def test_remove_task(self):
        self.heap.remove_task(1)
        self.assertDictEqual({3: [6, 3]}, self.heap.entry_finder)
        self.assertListEqual([5, self.heap.REMOVED], self.heap.pq[0])

    def test_pop_task(self):
        task, value = self.heap.pop_task()
        self.assertEqual(1, task)

    def test_pop_removed_task(self):
        self.heap.add_task(2, 1)
        self.heap.remove_task(2)
        task, value = self.heap.pop_task()
        self.assertEqual(1, task)

    def test_update_priority(self):
        self.heap.add_task(3, 2)
        self.assertDictEqual({1: [5, 1], 3: [2, 3]}, self.heap.entry_finder)
        self.assertListEqual([2, 3], self.heap.pq[0])
