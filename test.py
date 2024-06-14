# test_calculator.py
import unittest
from calculator import Calculator, MathOperations

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(1, 2), 3)
        self.assertEqual(self.calculator.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(2, 1), 1)
        self.assertEqual(self.calculator.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3, 3), 9)
        self.assertEqual(self.calculator.multiply(-1, 1), -1)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)

    def test_power(self):
        self.assertEqual(self.calculator.power(2, 3), 8)
        self.assertEqual(self.calculator.power(5, 0), 1)

    def test_square_root(self):
        self.assertEqual(self.calculator.square_root(9), 3)
        with self.assertRaises(ValueError):
            self.calculator.square_root(-1)

class TestMathOperations(unittest.TestCase):
    def setUp(self):
        self.math_operations = MathOperations()

    def test_evaluate_expression(self):
        self.assertEqual(self.math_operations.evaluate_expression("2 + 3 * 4"), 14)
        self.assertEqual(self.math_operations.evaluate_expression("10 / 2"), 5)
        self.assertEqual(self.math_operations.evaluate_expression("10 - 3 + 2"), 9)
        self.assertEqual(self.math_operations.evaluate_expression("2 ^ 3"), 8)
        self.assertEqual(self.math_operations.evaluate_expression("sqrt(9)"), 3)
        with self.assertRaises(ValueError):
            self.math_operations.evaluate_expression("10 / 0")
        with self.assertRaises(ValueError):
            self.math_operations.evaluate_expression("invalid expression")

if __name__ == '__main__':
    unittest.main()
