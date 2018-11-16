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

    if not data:
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

    if not data:
        raise ValueError("List cannot be empty!")
    sum_squares = sum([(i - calculate_mean(data)) ** 2 for i in data])
    return (sum_squares / len(data)) ** 0.5


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

    if not data:
        raise ValueError("List cannot be empty!")
    new_list = []
    mean = calculate_mean(data)
    s_d = calculate_standard_deviation(data)
    for i in data:
        if i >= (mean - 2 * s_d) and i <= (mean + 2 * s_d):
            new_list.append(i)
    return new_list
