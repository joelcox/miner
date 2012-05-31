import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import unittest

import miner.utils


class TestUtils(unittest.TestCase):

    def test_distance(self):
        # Wolfram `EuclidianDistance({1,2,3},{3,2,1}`
        self.assertEquals(miner.utils.distance((1, 2, 3), (3, 2, 1)),
                          2.8284271247461903)

    def test_gini(self):
        self.assertEquals(miner.utils.gini(0, 6), 0)
        self.assertEquals(miner.utils.gini(1, 5),
                          0.2777777777777777)
        self.assertEquals(miner.utils.gini(3, 3), 0.5)

    def test_entropy(self):
        self.assertEquals(miner.utils.entropy(0, 6), 0)
        self.assertEquals(miner.utils.entropy(1, 5),
                          0.6500224216483541)
        self.assertEquals(miner.utils.entropy(3, 3), 1)

    def test_classification_error(self):
        self.assertEquals(miner.utils.classification_error(0, 6), 0)
        self.assertEquals(miner.utils.classification_error(1, 5),
                          0.16666666666666663)
        self.assertEquals(miner.utils.classification_error(3, 3), 0.5)
