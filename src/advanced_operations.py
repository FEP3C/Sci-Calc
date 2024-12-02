import math


class AdvancedOperations:

    @staticmethod
    def square(a):
        return a ** 2

    @staticmethod
    def cube(a):
        return a ** 3

    @staticmethod
    def sqrt(a):
        if a < 0:
            raise ValueError("Cannot take square root of negative number")
        return math.sqrt(a)

    @staticmethod
    def cube_root(a):
        return a ** (1 / 3)

    @staticmethod
    def sin(a):
        return math.sin(math.radians(a))

    @staticmethod
    def cos(a):
        return math.cos(math.radians(a))

    @staticmethod
    def tan(a):
        return math.tan(math.radians(a))

    @staticmethod
    def ln(a):
        return math.log(a)

    @staticmethod
    def lg(a):
        return math.log10(a)

    @staticmethod
    def reciprocal(a):
        if a == 0:
            raise ValueError("Cannot take reciprocal of zero")
        return 1 / a

    @staticmethod
    def abs(a):
        return abs(a)

    @staticmethod
    def factorial(a):
        if not isinstance(a, int) or a < 0:
            raise ValueError("Factorial is not defined for negative numbers or non-integers")
        return math.factorial(a)
