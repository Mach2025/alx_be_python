import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test suite for SimpleCalculator class"""
    
    def setUp(self):
        """Initialize calculator before each test"""
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        """Test addition with various number combinations"""
        self.assertEqual(self.calc.add(2, 3), 5)          # Positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0)         # Negative and positive
        self.assertEqual(self.calc.add(0, 5), 5)          # Zero addition
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)     # Floats
        self.assertEqual(self.calc.add(-5, -3), -8)        # Negative numbers
    
    def test_subtraction(self):
        """Test subtraction with various number combinations"""
        self.assertEqual(self.calc.subtract(5, 3), 2)      # Positive result
        self.assertEqual(self.calc.subtract(3, 5), -2)     # Negative result
        self.assertEqual(self.calc.subtract(0, 5), -5)     # Zero minuend
        self.assertEqual(self.calc.subtract(2.5, 1.5), 1.0) # Floats
        self.assertEqual(self.calc.subtract(-5, -3), -2)    # Negative numbers
    
    def test_multiplication(self):
        """Test multiplication with various number combinations"""
        self.assertEqual(self.calc.multiply(2, 3), 6)      # Positive numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)    # Negative multiplier
        self.assertEqual(self.calc.multiply(0, 5), 0)      # Zero multiplication
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0) # Floats
        self.assertEqual(self.calc.multiply(-3, -3), 9)    # Negative numbers
    
    def test_division(self):
        """Test normal division scenarios"""
        self.assertEqual(self.calc.divide(6, 3), 2)        # Exact division
        self.assertEqual(self.calc.divide(5, 2), 2.5)       # Fractional result
        self.assertEqual(self.calc.divide(-6, 3), -2)       # Negative dividend
        self.assertEqual(self.calc.divide(0, 5), 0)         # Zero dividend
        self.assertEqual(self.calc.divide(1, 3), 1/3)       # Precise fractions
    
    def test_division_by_zero(self):
        """Test division by zero handling"""
        with self.assertRaises(ValueError):                # Using context manager
            self.calc.divide(5, 0)
        with self.assertRaises(ValueError):
            self.calc.divide(-10, 0)
    
    def test_invalid_input_types(self):
        """Test handling of non-numeric inputs"""
        with self.assertRaises(TypeError):
            self.calc.add("2", 3)
        with self.assertRaises(TypeError):
            self.calc.multiply(5, "a")
        with self.assertRaises(TypeError):
            self.calc.divide([1], 2)

if __name__ == '__main__':
    unittest.main()