'''graph.py'''

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self._nodes = nodes
        self._edges = edges
    def adjacentEdges(self, node):
        for edge in edges:
            continue

    @property
    def Edges(self):
        return self._edges

    @property
    def Nodes(self):
        return self._nodes


class Node:
    def __init__(self, data=None, pos = None):
        self._data = data
        self._pos = pos
class Edge:
    def __init__(self, nodeA=None, nodeB=None, data=None):
        self._value = (nodeA, nodeB)
        self._nodeA = self._value[0]
        self._nodeB = self._value[1]
        self._data = data

