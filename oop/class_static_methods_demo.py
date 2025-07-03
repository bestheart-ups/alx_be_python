# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Return the product of two numbers and print the calculation type."""
        print(f"Calculation Type: {cls.calculation_type}")
        return a * b

# Example usage
if __name__ == "__main__":
    # Using the static method
    result_add = Calculator.add(10, 5)
    print(f"Addition Result: {result_add}")

    # Using the class method
    result_multiply = Calculator.multiply(10, 5)
    print(f"Multiplication Result: {result_multiply}")
