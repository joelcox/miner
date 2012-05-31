import random

from miner.utils import distance as dist


class KMeans(object):

    def __init__(self, k, space):
        self.k = k
        self.space = space
        self.clusters = []
        self.iteration = 0

        # Set up our tree
        for k in range(self.k):
            self.clusters.append({'points': []})

    def converge(self, **kwargs):
        """Runs the algorithm for as much iterations
        to make the clusters converge
        """

        self.random_centroids()
        while True:
            self.compute_distances()
            self.assign_points()
            if self.compute_centroids() == False:
                break

        kwargs['render'](self.space, self.clusters)

    def random_centroids(self):
        """Selecter random centroids by generating random numbers,
        and adding the index to centroids list
        """

        amount = len(self.space.points) - 1
        self.centroids = []

        for k in range(self.k):
            centroid = self.space.points[(random.randint(0, amount))]
            self.centroids.append(centroid)
            amount -= 1

    def compute_distances(self):
        self.distances = []

        for point_index in range(len(self.space.points)):
            distance = []
            point = self.space.points[point_index]

            for centroid in self.centroids:
                distance.append(dist(centroid, point))

            self.distances.append(distance)

    def assign_points(self):
        """Loops over all points and assigns it to the correct cluster"""

        # Reset clusters
        self.clusters = []
        for k in range(self.k):
            self.clusters.append({'points': []})

        for point in range(len(self.space.points)):
            current_distances = self.distances.pop(0)
            lowest_distance = min(current_distances)
            cluster_index = current_distances.index(lowest_distance)
            self.clusters[cluster_index]['points'].append(point)

    def compute_centroids(self):

        centroids = []
        centroids.extend(self.centroids)
        self.previous_centroids = centroids
        self.iteration = self.iteration + 1

        # Compute the averages
        for cluster in range(len(self.clusters)):
            x = 0
            y = 0

            for point in self.clusters[cluster]['points']:
                x += self.space.points[point][0]
                y += self.space.points[point][1]

            # Make sure we don't device by zero
            length = len(self.clusters[cluster]['points'])
            if length != 0:
                self.centroids[cluster] = (x / length, y / length)
            else:
                self.centroids[cluster] = (x, y)

        # Do the centroids match?
        if self.centroids == self.previous_centroids:
            return False
