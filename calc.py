class calculator:
    """
    A simple calculator class to perform basic arithmetic operations.

    Methods:
        add(a, b):
            Returns the sum of a and b.
        sub(a, b):
            Returns the difference between a and b.
        mul(a, b):
            Returns the product of a and b.
        div(a, b):
            Returns the quotient of a divided by b.
        power(a, b):
            Returns a raised to the power of b.
    """
    def add(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
    def mul(self, a, b):
        return a * b
    def div(self, a, b):
        return a / b
    def power(self, a, b):
        return a ** b