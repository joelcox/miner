Miner
=====

Miner is a toy library for data mining. The main goal of this library is to provide an introduction to different data mining techniques while learning on the subject myself. This library isn't optimized for performance nor production use, but this might change at a later date. 

[![Build Status](https://secure.travis-ci.org/joelcox/miner.png?branch=master)](http://travis-ci.org/joelcox/miner)

K-means clustering 
------------------

A simple yet powerful algorithm for cluster analysis is the *k-means* algorithm. This algorithm will partition a set of objects over *k* clusters. You can run this algorithm using the code below. After the algorithm has converged, the `clusters` property of the `kmeans` objects (`kmeans.clusters`) will contain a dictionary with indexes that refer to the elements in `space.point`.

    import miner.utils
    import miner.clustering
    
    space = miner.utils.Space()
    space.points([(2, 2), (2, 1), (2, 3), (2, -2), (2, -1), (2, -3)])
    
    kmeans = miner.clustering.KMeans(2, space)
    kmeans.converge()

K-nearest neighbor
------------------

If you want to classify a certain record by comparing it to training data, you can employ a classification algorithm, like *KNN*. This simple algorithm allows calculates the distance between the record to be classified and the training records. The algorithm will return the class label which is most common for the *k* nearest records.

    import miner.utils
    import miner.classification
    
    matrix = miner.utils.Matrix(4)
    matrix.records([[1.0, 2.3, 5.0, 3.0],
                   [2.0, 4.0, 1.2, 1.8],
                   [15.0, 12.2, 13.0, 1.1],
                   [10.0, 9.4, 8.4, 1.],
                   [-10.0, 3.2, 1.6, -1.0],
                   [-1.0, 2.2, 1.2, -3.0]])
    # Associate the class label with the records
    matrix.classes(['A', 'A', 'B', 'B', 'C', 'C'])
    
    knn = miner.classification.KNearestNeighbor(3, matrix)
    print knn.classify([1.2, 4.2, 4.2, -1.2])

License
-------
This library is released under the MIT license.