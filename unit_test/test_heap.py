from unittest import TestCase, main

from tools.heap import Heap


class TestHeap(TestCase):
    def setUp(self):
        self.heap = Heap([[5, 'A'], [6, 'C']])

    def tearDown(self):
        self.heap = None

    def test_add_task(self):
        self.heap.add_task('B', 1)
        self.assertDictEqual({'A': [5, 'A'], 'B': [1, 'B'], 'C': [6, 'C']}, self.heap.entry_finder)
        self.assertListEqual([1, 'B'], self.heap.pq[0])

    def test_remove_task(self):
        self.heap.remove_task('A')
        self.assertDictEqual({'C': [6, 'C']}, self.heap.entry_finder)
        self.assertListEqual([5, self.heap.REMOVED], self.heap.pq[0])

    def test_pop_task(self):
        task, value = self.heap.pop_task()
        self.assertEqual('A', task)

    def test_pop_removed_task(self):
        self.heap.add_task('B', 1)
        self.heap.remove_task('B')
        task, value = self.heap.pop_task()
        self.assertEqual('A', task)

    def test_update_priority(self):
        self.heap.add_task('C', 2)
        self.assertDictEqual({'A': [5, 'A'], 'C': [2, 'C']}, self.heap.entry_finder)
        self.assertListEqual([2, 'C'], self.heap.pq[0])


if __name__ == '__main__':
    main()
