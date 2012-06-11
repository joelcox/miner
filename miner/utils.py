from __future__ import division
import math

import numpy


class Space(object):
    def __init__(self, dimension=2):
        if dimension < 2:
            raise ValueError('Dimension can\'t be smaller than 2')

        self.dimension = dimension
        self.array = []

    def points(self, *args):
        """Appends a point to the point lists and verifies
        its dimension.
        """
        if (isinstance(args[0], list)):
            for tup in args[0]:
                self.points(*tup)
            return

        if len(args) != self.dimension:
            raise IndexError('Amount of arguments (%s) does not match space \
                              dimension (%s)' % (len(args), self.dimension))

        floats = map(float, args)
        self.array.append(tuple(floats))


class Matrix(Space):

    def records(self, records):
        """Sets the array with records."""
        array = numpy.array(records)

        # Edge case for matrixes with only one record
        try:
            attributes = array.shape[1]
        except IndexError:
            attributes = array.shape[0]

        if attributes != self.dimension:
            raise IndexError('Amount of attributes (%s) does not match \
                              matrix dimension (%s)' %
                              (array.shape[1], self.dimension))

        self.array = array

    def classes(self, classes):
        """Sets a list of classes for the coressponding
        points"""

        if len(classes) != len(self.array):
            raise IndexError('Amount of classes (%s) does not match the \
                              amount of records (%s)' %
                              (len(classes), len(self.array)))

        self.classes = classes


def distance(p, q):
    """ Computes the Euclidian distance between two points
    """
    if len(p) != len(q):
        raise IndexError('The dimension of the two points don\'t match')

    total = 0
    for i in range(len(p)):
        total += (p[i] - q[i]) ** 2

    return math.sqrt(total)


def gini(p, q):
    """ Computes the Gini index between two numbers
    """
    # TODO: generalize to arbitrary number of points
    total = p + q
    return 1 - (p / total) ** 2 - (q / total) ** 2


def entropy(p, q):
    """ Computes the Entropy between two numbers
    """
    total = p + q

    # TODO: generalize to arbitrary number of points
    try:
        p_log = math.log(p / total, 2)
    except ValueError:
        p_log = 0

    try:
        q_log = math.log(q / total, 2)
    except ValueError:
        q_log = 0

    return -(p / total) * p_log - (q / total) * q_log


def classification_error(p, q):
    """ Computers the classification error rate
    """
    total = p + q
    return 1 - max(p / total, q / total)
