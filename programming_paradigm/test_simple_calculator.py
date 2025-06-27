# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Test cases for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method with various scenarios."""
        # Basic addition
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)

        # Edge cases
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)

        # Large numbers
        self.assertEqual(self.calc.add(1000000, 2000000), 3000000)

        # Decimal numbers
        self.assertAlmostEqual(self.calc.add(2.5, 3.7), 6.2, places=7)

    def test_subtraction(self):
        """Test the subtraction method with various scenarios."""
        # Basic subtraction
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 10), 0)
        self.assertEqual(self.calc.subtract(-5, -3), -2)

        # Edge cases
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 0), 0)

        # Negative results
        self.assertEqual(self.calc.subtract(3, 8), -5)

        # Decimal numbers
        self.assertAlmostEqual(self.calc.subtract(7.8, 2.3), 5.5, places=7)

    def test_multiplication(self):
        """Test the multiplication method with various scenarios."""
        # Basic multiplication
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(-2, -6), 12)

        # Edge cases
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)

        # Identity multiplication
        self.assertEqual(self.calc.multiply(7, 1), 7)
        self.assertEqual(self.calc.multiply(1, 7), 7)

        # Large numbers
        self.assertEqual(self.calc.multiply(1000, 1000), 1000000)

        # Decimal numbers
        self.assertAlmostEqual(self.calc.multiply(2.5, 4.0), 10.0, places=7)

    def test_division(self):
        """Test the division method with various scenarios."""
        # Basic division
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(15, 3), 5.0)
        self.assertEqual(self.calc.divide(-12, 3), -4.0)
        self.assertEqual(self.calc.divide(-12, -3), 4.0)

        # Division resulting in decimals
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5, places=7)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.333333333333, places=7)

        # Edge cases
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(5, 1), 5.0)

        # Division by zero - should return None
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

        # Decimal numbers
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0, places=7)

    def test_edge_cases_comprehensive(self):
        """Test comprehensive edge cases across all operations."""
        # Very large numbers
        large_num = 1e10
        self.assertEqual(self.calc.add(large_num, large_num), 2e10)
        self.assertEqual(self.calc.subtract(large_num, large_num), 0)
        self.assertEqual(self.calc.multiply(large_num, 2), 2e10)
        self.assertEqual(self.calc.divide(large_num, large_num), 1.0)

        # Very small numbers
        small_num = 1e-10
        self.assertAlmostEqual(self.calc.add(small_num, small_num), 2e-10, places=15)
        self.assertAlmostEqual(self.calc.subtract(small_num, small_num), 0, places=15)
        self.assertAlmostEqual(self.calc.multiply(small_num, 2), 2e-10, places=15)
        self.assertAlmostEqual(self.calc.divide(small_num, small_num), 1.0, places=15)


if __name__ == '__main__':
    # Run the tests
    unittest.main()