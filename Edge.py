#This class is used to represent a weighted edge of a graph. If e_1, e_2 are
#two instances of Edge, then e_1 < e_2, e_1 > e_2, e_1 == e_2 are all evaluated
#according to the respective weights of e_1 and e_2. This allows you to create
#a minHeap full of Edge objects sorted by weight, which is a helpful data
#structure in several important graph algorithms.

#It is also possible to compare Edge objects to ints and floats,
#where the result is again determined by the weight of the edge,

class Edge:

    def __init__(self, source, target, weight = 1):
        
        self.source = source
        self.target = target
        self.weight = weight

    def __eq__(self, other):
        
        if isinstance(other, Edge):
            return self.weight == other.weight
        if isinstance(other, float):
            return self.weight == other
        if isinstance(other, int):
            return self.weight == other

    def __lt__(self, other):
        
        if isinstance(other, Edge):
            return self.weight < other.weight
        if isinstance(other, float):
            return self.weight < other
        if isinstance(other, int):
            return self.weight < other

    def __gt__(self, other):
        
        if isinstance(other, Edge):
            return self.weight > other.weight
        if isinstance(other, float):
            return self.weight > other
        if isinstance(other, int):
            return self.weight > other
