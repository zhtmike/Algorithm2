from os.path import join
from unittest import TestCase

from assign5 import Assign5

assign5_dir = '../data/assign5/test_case/'


class TestAssign5(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.assign5 = Assign5()
        cls.text_sample1 = join(assign5_dir, 'q11.txt')
        cls.text_sample2 = join(assign5_dir, 'q12.txt')
        cls.text_sample3 = join(assign5_dir, 'q13.txt')

    @classmethod
    def tearDownClass(cls):
        cls.assign5 = None

    def test_question(self):
        self.assertEqual(6, self.assign5.question(self.text_sample1))
        self.assertEqual(7, self.assign5.question(self.text_sample2))
        self.assertEqual(8387, self.assign5.question(self.text_sample3))
