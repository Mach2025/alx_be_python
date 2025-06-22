# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method to add two numbers"""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method to multiply two numbers and display calculation type"""
        print(f"Calculation Type: {cls.calculation_type}")
        return a * b


# Example usage
if __name__ == "__main__":
    # Using static method
    result_add = Calculator.add(5, 3)
    print(f"Addition Result: {result_add}")

    # Using class method
    result_multiply = Calculator.multiply(4, 6)
    print(f"Multiplication Result: {result_multiply}")
