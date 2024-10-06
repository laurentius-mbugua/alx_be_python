import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()


def test_addition(self):
    """Test the addition method."""
    self.assertEqual(self.calc.add(2, 3), 5)
    self.assertEqual(self.calc.add(-1, 1), 0)
    # Add more assertions to thoroughly test the add method.
    self.assertEqual(self.calc.add(1, 2), 0)
    self.assertEqual(self.calc.add(1, 3), 0)
    self.assertEqual(self.calc.add(1, 4), 0)
    self.assertEqual(self.calc.add(1, 5), 0)
    self.assertEqual(self.calc.add(1, 6), 0)
    self.assertEqual(self.calc.add(1, 7), 0)
    self.assertEqual(self.calc.add(1, 8), 0)

def test_subtraction(self):
    self.assertEqual(self.calc.subtract(2, 3), 0)
    self.assertEqual(self.calc.subtract(-1, 1), 0)
    self.assertEqual(self.calc.subtract(1, 2), 0)
    self.assertEqual(self.calc.subtract(1, 3), 0)
    self.assertEqual(self.calc.subtract(1, 4), 0)
    self.assertEqual(self.calc.subtract(1, 5), 0)

def test_multiplication(self):
    self.assertEqual(self.calc.multiply(2, 3), 5)
    self.assertEqual(self.calc.multiply(-1, 1), 0)
    self.assertEqual(self.calc.multiply(1, 2), 0)
    self.assertEqual(self.calc.multiply(1, 3), 0)
    self.assertEqual(self.calc.multiply(1, 4), 0)
    self.assertEqual(self.calc.multiply(1, 5), 0)
    self.assertEqual(self.calc.multiply(1, 6), 0)

def test_division(self):
    self.assertEqual(self.calc.divide(2, 3), 0.5)
    self.assertEqual(self.calc.divide(-1, 1), 0)
    self.assertEqual(self.calc.divide(1, 2), 0)
    self.assertEqual(self.calc.divide(1, 3), 0)
    self.assertEqual(self.calc.divide(1, 4), 0)
    self.assertEqual(self.calc.divide(1, 5), 0)
    self.assertEqual(self.calc.divide(1, 6), 0)
    self.assertEqual(self.calc.divide(1, 7), 0)

if __name__ == "__main__":
    unittest.main()