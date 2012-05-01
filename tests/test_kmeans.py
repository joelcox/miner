import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import unittest

import miner.utils
import miner.clustering


class TestSpace(unittest.TestCase):

    def setUp(self):
        space = miner.utils.Space()
        space.point([(2, 2), (2, 1), (2, 3), (2, -2), (2, -1), (2, -3)])
        
        self.kmeans = miner.clustering.KMeans(2, space)
        
    def test_amount_centroids(self):
        self.kmeans.random_centroids()
        self.assertEquals(len(self.kmeans.centroids), 2)
        self.assertTrue(map(lambda x: x < len(self.kmeans.centroids),
                            self.kmeans.centroids))
                            
    def test_assign_points(self):
        # Manually set our centroids, instead of random, so
        # we can predict the output
        self.kmeans.centroids = [(2, 2), (2, -2)]
        
        self.kmeans.compute_distances();
        self.kmeans.assign_points()
        
        self.assertEquals(self.kmeans.clusters,
                          [ {'points': [0, 1, 2]}, 
                            {'points': [3, 4, 5]}])
        
