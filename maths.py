"""
This file contains a set of functions to practice your
maths skills.

It needs to be completed with "vanilla" Python, without
help from any library.
"""


def derivative(w1, w2, x):
    """
    Given the following function f(x) = w1 * x^3 + w2 * x - 1
    evaluate the derivative of the function on x

    :param w1: first coefficient
    :param w2: second coefficient
    :param x: point on which to evaluate derivative (float)
    :return: value of the derivative on point x
    :rtype: float
    """

    return float(3 * w1 * x ** 3 + w2)


def abs_dist(x):
    """
    Return the absolute value of x

    :param x: a number (float)
    :return: absolute value of x
    :rtype: float
    """

    if x < 0:
        x = -x
    return float(x)


def fact(x):
    """
    Return the factorial of x.
    Your function should raise a ValueError
    if x is negative

    :param x: a number (int)
    :return: the factorial of x
    :rtype: float
    :raise ValueError:
    """

    if x < 0:
        raise ValueError("Number cannot be negative!")
    x_fact = 1
    for i in range(1, x + 1):
        x_fact *= i
    return float(x_fact)


def combination(n, r):
    """
    Given n total number of items,
    what is the number of possible ways
    to choose r items from it?

    :param n: total number of items (integer)
    :param r: number of items to arrange (int)
    :return: number of combinations
    :rtype: integer
    """

    x = fact(n)
    x_n = fact(n - r)
    x_r = fact(r)
    return int(x / (x_n * x_r))
