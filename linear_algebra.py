"""
This file contains a set of functions to practice your
linear algebra skills.
It needs to be completed with "vanilla" Python, without
help from any library.
"""


def gradient(w1, w2, x):
    """
    Given the following function f(x) = w1 * x1^2 + w2 * x2
    where x is a vector with coordinates [x1, x2]
    evaluate the gradient of the function at the point x

    :param w1: first coefficient
    :param w2: second coefficient
    :param x: a point represented by a tuple (x1, x2)
    :return: the two coordinates of gradient of f
    at point x
    :rtype: float, float
    """

    return (2 * w1 * x[0], w2)


def metrics(u, v):
    """
    Given two vectors, evaluate the following metrics and return two arguments:
    - l1 Distance
    - l2 Distance

    If the two vectors have a different dimension,
    you should raise a ValueError

    :param u: first vector (list)
    :param v: second vector (list)
    :return: l1 distance, l2 distance
    :rtype: float, float
    :raise ValueError:
    """

    if len(u) != len(v):
        raise ValueError("Vector dimensions not compatible!")
    l_1 = [abs(i_u - i_v) for i_u, i_v in zip(u, v)]
    l_1 = sum(l_1)
    l_2 = [(i_u - i_v)**2 for i_u, i_v in zip(u, v)]
    l_2 = sum(l_2) ** 0.5
    return l_1, l_2


def list_mul(u, v):
    """
    Given two vectors, calculate and return the following quantities:
    - element-wise sum
    - element-wise product
    - dot product

    If the two vectors have a different dimension,
    you should raise a ValueError

    :param u:first vector (list)
    :param v:second vector (list)
    :return:the three quantities above
    :rtype: list, list, float
    :raise ValueError:
    """

    if len(u) != len(v):
        raise ValueError("Vector dimensions not compatible!")
    e_sum = [i_u + i_v for i_u, i_v in zip(u, v)]
    e_prod = [i_u * i_v for i_u, i_v in zip(u, v)]
    return e_sum, e_prod, float(sum(e_prod))


def matrix_mul(A, B):
    """
    Given two matrices A and B represented as a list of list,
    implement a function to multiply them together (A * B)

    For example:
    A = [[1, 2, 3],
          [4, 5, 6]]
    is a matrix with twp rows and three columns.

    If the two matrices have incompatible dimensions,
    you should raise a ValueError

    :param A: first matrix (list of list)
    :param B: second matrix (list of list)
    :return: resulting matrix (list of list)
    :rtype: list(list)
    :raise ValueError:
    """

    if len(A[0]) != len(B):
        raise ValueError("Matrix dimensions not compatible!")
    m_m = len(A)
    n_m = len(A[0])
    r_m = len(B[0])
    m_c = [[0 for i in range(r_m)] for j in range(m_m)]
    for i in range(m_m):
        for j in range(r_m):
            for k in range(n_m):
                m_c[i][j] += A[i][k] * B[k][j]
    return m_c
