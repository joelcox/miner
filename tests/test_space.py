import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import unittest

import miner.utils


class TestSpace(unittest.TestCase):

    def setUp(self):
        self.space = miner.utils.Space(3)

    def test_float_conversion(self):
        self.space.points(1, 2, 3)
        self.assertEqual(self.space.array, [(1.00, 2.00, 3.00)])

    def test_tuple_points(self):
        self.space.points([(1, 2, 3), (3, 2, 1)])
        self.assertEqual(len(self.space.array), 2)

    def test_dimension_mismatch(self):
        self.assertRaises(IndexError, self.space.points, (1.00, 2.00))
