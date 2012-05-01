import math
from types import ListType

class Space(object):
    def __init__(self, dimension=2):
        if dimension < 2:
            raise ValueError('Dimension can\'t be smaller than 2')
        
        self.dimension = dimension
        self.points = []

    def point(self, *args):
        """Appends a point to the point lists and verifies
        its dimension.
        """
        if (type(args[0]) is ListType):
            for tup in args[0]:
                self.point(*tup)
            return
        
        if len(args) != self.dimension:
            raise IndexError('Amount of arguments (%s) does not match space \
                              dimension (%s)' % (len(args), self.dimension))

        floats = map(float, args)
        self.points.append(tuple(floats))

def distance(p, q):
    """
    Compute the Euclidian distance between two points
    """
    if len(p) != len(q):
        raise IndexError('The dimension of the two points don\'t match')
    
    total = 0
    for i in range(len(p)):
        total += (p[i] - q[i])**2
    
    return math.sqrt(total)