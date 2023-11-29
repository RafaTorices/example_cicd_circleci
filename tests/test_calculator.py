# Test file for calculator.py
# Python App to do basic math operations

"""
File to test the calculator.py file
"""

# Import function of the calculator.py file
from src import calculator


def test_addition():
    """
    Function to test the add function
    """
    assert 4.5 == calculator.add(2.5, 2.0)


def test_subtraction():
    """
    Function to test the subtract function
    """
    assert 0 == calculator.subtract(4, 4)


def test_multiplication():
    """
    Function to test the multiply function
    """
    assert 1000 == calculator.multiply(100, 10)


def test_division():
    """
    Function to test the divide function
    """
    assert 5 == calculator.divide(25, 5)


def test_mathpow():
    """
    Function to test the mathpow function
    """
    assert 100 == calculator.mathpow(10, 2)
