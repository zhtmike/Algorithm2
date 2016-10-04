from unittest import main, TestCase

from assign1 import Assign1


class TestAssign1(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.assign1 = Assign1()
        cls.text_location = '../data/test_case/q11.txt'
        cls.test_list = [[10, 1], [5, 5], [6, 6], [1, 10]]

    @classmethod
    def tearDownClass(cls):
        pass

    def test_read_txt(self):
        text_list = self.assign1.read_txt(self.text_location)
        self.assertListEqual(text_list, self.test_list)

    def test_question_one(self):
        value = self.assign1.question_one(self.text_location)
        self.assertEqual(value, 134)

    def test_question_two(self):
        value = self.assign1.question_two(self.text_location)
        self.assertEqual(value, 134)


if __name__ == '__main__':
    main()
