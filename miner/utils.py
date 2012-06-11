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

        self.class_labels = classes

    def normalize(self):
        """Normalizes all columns in the matrix so that the standard deviation
        per column is equal to one."""

        # Compute the current mean and standard deviation for each column
        for column_index in range(self.dimension):

            column = self.array[0:, column_index]
            mean = column.mean()
            std = column.std()

            # Compute the new value for the element, considering the
            # mean and std deviation.
            for row_index in range(column.shape[0]):
                element = self.array[row_index, column_index]
                self.array[row_index, column_index] = (element - mean) / std


class CappedOrderedList(object):
    """A list with a fixed size that maintains order"""

    def __init__(self, length=3):
        self.list = []
        self.length = length

    def add(self, item):
        """Adds a new item to the list"""
        try:
            value = item[0]
        except TypeError:
            value = item

        # Check whether and where we insert the new item
        insert_position = self._find_insert_position(value)

        if insert_position is not False:
            self.list.insert(insert_position, item)
            self._maintain_length()

    def _find_insert_position(self, value):
        """Computes at which position a new item should be inserted"""
        if len(self.list) == 0:
            return 0

        for index in range(len(self.list)):
            item = self.list[index]

            try:
                existing_value = item[0]
            except TypeError:
                existing_value = item

            if value <= existing_value:
                return index

        # Make sure to append if the list isn't full yet
        if self.length != len(self.list):
            return len(self.list)
        return False

    def _maintain_length(self):
        """Ensures that the length of the list is never longer
        than the max"""
        if self.length < len(self.list):
            self.list.pop()

    def __len__(self):
        """Returns the length of the internal list"""
        return len(self.list)

    def __getitem__(self, index):
        """Returns the element at the given location in the internal list"""
        return self.list[index]

    def __str__(self):
        return str(self.list)

    def __iter__(self):
        return self.list.__iter__()


def distance(p, q):
    """ Computes the Euclidian distance between two points"""
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
