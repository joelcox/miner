import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import unittest

import miner.utils
import miner.classification


class TestKNearestNeighbor(unittest.TestCase):

    def setUp(self):
        matrix = miner.utils.Matrix(3)
        matrix.records([[1.0, 2, 30], [2, 8, 6], [4, 5, 100]])
        matrix.classes(['A', 'A', 'B'])
        self.knn = miner.classification.KNearestNeighbor(3, matrix)

    def test_passed_matrix(self):
        # You can only pass a Matrix, not a Space
        space = miner.utils.Space()
        space.points(2, 3)
        self.assertRaises(TypeError,  miner.classification.KNearestNeighbor,
                          3, space)

    def test_attributes_mismatch(self):
        self.assertRaises(IndexError, self.knn.classify, [1, 2])

    def test_most_common(self):
        self.knn.nearest = miner.utils.CappedOrderedList(5)
        self.knn.nearest.add(('100', 'A'))
        self.knn.nearest.add(('100', 'A'))
        self.knn.nearest.add(('100', 'A'))
        self.knn.nearest.add(('100', 'B'))
        self.knn.nearest.add(('100', 'B'))

        self.assertEqual(self.knn._most_common_class(), 'A')

    def test_classification(self):
        self.knn.matrix.classes(['A', 'A', 'B'])
        self.assertEqual(self.knn.classify([1, 4, 5]), 'A')

    def test_classification_cosine(self):
        self.knn.matrix.classes(['A', 'A', 'B'])
        self.knn.function = miner.utils.similarity
        self.assertEqual(self.knn.classify([1, 4, 5]), 'A')
