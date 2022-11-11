import unittest


class NumbersTest(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(1 + 1, 1)  # Тест сравнивает два числа в круглых скобках


if __name__ == '__main__':
    unittest.main()
