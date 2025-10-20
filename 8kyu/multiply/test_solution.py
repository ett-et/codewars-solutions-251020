import unittest
from solution import multiply


class TestMultiply(unittest.TestCase):
    def test_basic_examples(self):
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(2, 4), 8)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(5, 0), 0)
    
    def test_negative_numbers(self):
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(-5, -5), 25)
    
    def test_decimals(self):
        self.assertEqual(multiply(2.5, 4), 10.0)


if __name__ == '__main__':
    unittest.main()
