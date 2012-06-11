import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import unittest

import miner.utils
import miner.classification


class TestKNearestNeighbor(unittest.TestCase):

    def test_passed_matrix(self):
        space = miner.utils.Space()
        space.points(2, 3)
        self.assertRaises(TypeError,  miner.classification.KNearestNeighbor,
                          3, space)
