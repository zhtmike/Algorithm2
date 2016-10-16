from os.path import join
from unittest import TestCase

from assign2 import Assign2

assign2_dir = '../data/assign2/test_case/'


class TestAssign2(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.assign2 = Assign2()
        cls.text_sample1 = join(assign2_dir, 'q11.txt')

    @classmethod
    def tearDownClass(cls):
        cls.assign1 = None

    def test_question_one(self):
        self.assertEqual(273, self.assign2.question_one(self.text_sample1, 3))
