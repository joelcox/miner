import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import unittest

import miner.utils


class TestMatrix(unittest.TestCase):

    def setUp(self):
        self.matrix = miner.utils.Matrix(3)

    def test_single_record(self):
        # NumPy does some funky stuff with the shape
        # for matrixes with a single row
        self.matrix.records([1, 2, 3])
        self.assertEqual(self.matrix.array.shape, (3,))

    def test_tuple_points(self):
        self.matrix.records([[1, 2, 3], [3, 2, 1]])
        self.assertEqual(len(self.matrix.array), 2)

    def test_dimension_mismatch(self):
        self.assertRaises(IndexError, self.matrix.records, [1.00, 2.00])

    def test_classes_mismatch(self):
        self.matrix.records([[1, 2, 3], [3, 2, 1]])
        self.assertRaises(IndexError, self.matrix.classes, ['A'])
