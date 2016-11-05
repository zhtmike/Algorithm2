from os.path import join
from unittest import TestCase

from assign4 import Assign4

assign4_dir = '../data/assign4/test_case/'


class TestAssign4(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.assign4 = Assign4()
        cls.text_samples = [join(assign4_dir, 'q11.txt'), join(assign4_dir, 'q12.txt')]

    @classmethod
    def tearDownClass(cls):
        cls.assign4 = None

    def test_question(self):
        values = self.assign4.question(self.text_samples)
        self.assertListEqual([-10003, -6], values)
