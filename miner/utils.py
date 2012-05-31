from __future__ import division
import math
import types


class Space(object):
    def __init__(self, dimension=2):
        if dimension < 2:
            raise ValueError('Dimension can\'t be smaller than 2')

        self.dimension = dimension
        self.points = []

    def point(self, *args):
        """Appends a point to the point lists and verifies
        its dimension.
        """
        if (type(args[0]) is types.ListType):
            for tup in args[0]:
                self.point(*tup)
            return

        if len(args) != self.dimension:
            raise IndexError('Amount of arguments (%s) does not match space \
                              dimension (%s)' % (len(args), self.dimension))

        floats = map(float, args)
        self.points.append(tuple(floats))


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
