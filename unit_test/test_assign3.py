from os.path import join
from unittest import TestCase

from assign3 import Assign3

assign3_dir = '../data/assign3/test_case/'


class TestAssign3(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.assign3 = Assign3()
        cls.text_sample1 = join(assign3_dir, 'q11.txt')

    @classmethod
    def tearDownClass(cls):
        cls.assign3 = None

    def test_question(self):
        self.assertEqual(35, self.assign3.question(self.text_sample1))
