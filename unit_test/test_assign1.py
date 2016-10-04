from unittest import main, TestCase

from assign1 import Assign1


class TestAssign1(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.assign1 = Assign1()
        cls.text_sample1 = '../data/test_case/assign1/q11.txt'
        cls.text_sample2 = '../data/test_case/assign1/q12.txt'
        cls.text_sample3 = '../data/test_case/assign1/q13.txt'

    @classmethod
    def tearDownClass(cls):
        pass

    def test_question_one(self):
        # use difference approach
        self.assertEqual(self.assign1.question_one(self.text_sample1), 31814)
        self.assertEqual(self.assign1.question_one(self.text_sample2), 61545)
        self.assertEqual(self.assign1.question_one(self.text_sample3), 688647)

    def test_question_two(self):
        # use ratio approach
        self.assertEqual(self.assign1.question_two(self.text_sample1), 31814)
        self.assertEqual(self.assign1.question_two(self.text_sample2), 60213)
        self.assertEqual(self.assign1.question_two(self.text_sample3), 674634)


if __name__ == '__main__':
    main()
