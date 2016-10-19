from unittest import TestCase

from cython_module.union_find import UnionFind


class TestUnionFinder(TestCase):
    def setUp(self):
        self.uf = UnionFind(4)

    def tearDown(self):
        self.uf = None

    def test_merge(self):
        self.uf.merge(1, 2)
        self.assertEqual(1, self.uf.find(2))
        self.uf.merge(0, 1)
        self.assertEqual(1, self.uf.find(0))
        self.assertEqual(3, self.uf.find(3))
        self.uf.merge(0, 3)
        self.assertEqual(1, self.uf.find(3))
