"""
This file contains a set of functions to practice your
statistics skills.

It needs to be completed with "vanilla" Python, without
help from any library.
"""


def calculate_mean(data):
    """
    Return the mean of a python list

    If data is empty raise a ValueError

    :param data: a list of numbers
    :return: the mean of the list
    :rtype: float
    :raise ValueError:
    """

    if len(data) == 0:
        raise ValueError("List can not be empty!")
    return sum(data) / len(data)


def calculate_standard_deviation(data):
    """
    Return the standard deviation of a python list

    If data is empty raise a ValueError

    :param data: list of numbers
    :return: the standard deviation of the list
    :rtype: float
    :raise ValueError:
    """

    if len(data) == 0:
        raise ValueError("List cannot be empty!")
    return (sum([(i - calculate_mean(data)) ** 2 for i in data]) / len(data)) ** 0.5


def remove_outliers(data):
    """
    Given a list of numbers, find outliers and return a new
    list that contains all points except outliers
    We consider points lying outside 2 standard
    deviations from the mean.

    Make sure that you do not modify the original list!

    If data is empty raise a ValueError

    :param data: list of numbers
    :return: a new list without outliers
    :rtype: list
    :raise ValueError:
    """

    if len(data) == 0:
        raise ValueError("List cannot be empty!")
    return [i for i in data if i >= (calculate_mean(data) - 2 * calculate_standard_deviation(
        data)) and i <= (calculate_mean(data) + 2 * calculate_standard_deviation(data))]
