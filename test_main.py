# test_main.py
import unittest
from unittest.mock import patch
from main import calculator

class TestCalculator(unittest.TestCase):
    @patch('builtins.input', side_effect=["1", "5", "3"])
    def test_addition(self, input):
        self.assertEqual(calculator(), 8)

    @patch('builtins.input', side_effect=["2", "5", "3"])
    def test_subtraction(self, input):
        self.assertEqual(calculator(), 2)

    @patch('builtins.input', side_effect=["3", "5", "3"])
    def test_multiplication(self, input):
        self.assertEqual(calculator(), 15)

    @patch('builtins.input', side_effect=["4", "6", "3"])
    def test_division(self, input):
        self.assertEqual(calculator(), 2)

    @patch('builtins.input', side_effect=["5", "5", "3"])
    def test_invalid_operation(self, input):
        self.assertEqual(calculator(), "Invalid operation")

if __name__ == '__main__':
    unittest.main()