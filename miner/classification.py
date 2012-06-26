import miner.utils


class KNearestNeighbor(object):

    def __init__(self, k, matrix, function=miner.utils.distance):
        if isinstance(matrix, miner.utils.Matrix) is False:
            raise TypeError('A matrix should be passed as the second argument')

        self.k = k
        self.matrix = matrix
        self.function = function

    def classify(self, record):
        """Classifies a certain record by looking at the nearest records"""
        ascending = True if self.function.__name__ != 'similarity' else False
        self.nearest = miner.utils.CappedOrderedList(self.k, ascending)

        if len(record) != self.matrix.dimension:
            raise IndexError('Amount of attributes (%s) does not match \
                matrix dimension (%s)' % (len(record), self.matrix.dimension))

        # Normalize the record using the known mean and std of the columns,
        # but only if the matrix is normalized
        if self.matrix.normalized is True:

            normalized_record = []
            for index in range(len(record)):
                mean = self.matrix.column_stats[index][0]
                std = self.matrix.column_stats[index][0]

                normalized_record.append((record[index] - mean) / std)

            record = normalized_record

        # Calculate the distance between the the record and training data
        for index in range(self.matrix.array.shape[0]):
            matrix_record = self.matrix.array[index]
            distance = self.function(record, matrix_record)
            self.nearest.add((distance, self.matrix.class_labels[index]))

        return self._most_common_class()

    def _most_common_class(self):
        """Counts all compared classes, tallies and figures out which
        appeared most"""

        appearances = {}

        # Count all labels
        for record in self.nearest:
            if record[1] in appearances:
                appearances[record[1]] = appearances[record[1]] + 1
            else:
                appearances[record[1]] = 1

        # Find the most seen label
        most_seen = ('', 0)
        for label, count in appearances.iteritems():
            if count > most_seen[1]:
                most_seen = (label, count)

        return most_seen[0]
