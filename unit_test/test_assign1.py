from os.path import join
from unittest import TestCase

from assign1 import Assign1

assign1_dir = '../data/assign1/test_case/'


class TestAssign1(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.assign1 = Assign1()
        cls.text_sample1 = join(assign1_dir, 'q11.txt')
        cls.text_sample2 = join(assign1_dir, 'q12.txt')
        cls.text_sample3 = join(assign1_dir, 'q13.txt')
        cls.graph_sample1 = join(assign1_dir, 'q31.txt')

    @classmethod
    def tearDownClass(cls):
        cls.assign1 = None

    def test_question_one(self):
        # use difference approach
        self.assertEqual(31814, self.assign1.question_one(self.text_sample1))
        self.assertEqual(61545, self.assign1.question_one(self.text_sample2))
        self.assertEqual(688647, self.assign1.question_one(self.text_sample3))

    def test_question_two(self):
        # use ratio approach
        self.assertEqual(31814, self.assign1.question_two(self.text_sample1))
        self.assertEqual(60213, self.assign1.question_two(self.text_sample2))
        self.assertEqual(674634, self.assign1.question_two(self.text_sample3))

    def test_question_three(self):
        self.assertEqual(12, self.assign1.question_three(self.graph_sample1))
