Miner
=====

Miner is a toy library for data mining. The main goal of this library is to provide an introduction to different data mining techniques while learning on the subject myself. This library isn't optimized for performance nor production use, but this might change at a later date. 

[![Build Status](https://secure.travis-ci.org/joelcox/miner.png?branch=master)](http://travis-ci.org/joelcox/miner)

Quick start
-----------

A simple yet powerful algorithm for cluster analysis is the *k-means* algorithm. This algorithm will partition a set of objects over *k* clusters. You can run this algorithm using the code below. After the algorithm has converged, the `clusters` property of the `kmeans` objects (`kmeans.clusters`) will contain a dictionary with indexes that refer to the elements in `space.point`.

    import miner.utils
    import miner.clustering
    
    space = miner.utils.Space()
    space.points([(2, 2), (2, 1), (2, 3), (2, -2), (2, -1), (2, -3)])
    
    kmeans = miner.clustering.KMeans(2, space)
    kmeans.converge()
    
License
-------
This library is released under the MIT license.