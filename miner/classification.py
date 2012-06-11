import miner.utils


class KNearestNeighbor(object):

    def __init__(self, k, matrix):
        if isinstance(matrix, miner.utils.Matrix) is False:
            raise TypeError('A matrix should be passed as the second argument')

        self.k = k
        self.matrix = matrix
