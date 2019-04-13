'''graph.py'''


class Graph(object):
    '''docstring'''

    def __init__(self, nodes=None, edges=None):
        '''docstring'''
        self._nodes = nodes
        self._edges = edges

    @property
    def edges(self):
        '''edges'''
        return self._edges

    @property
    def nodes(self):
        '''nodes'''
        return self._nodes

    def adjacentEdges(self, node):
        '''docstring'''
        adjacents = []
        for edge in self.edges:
            if node in edge:
                adjacents.append(edge[0])
                adjacents.append(edge[1])
            adjacents.remove(node)


class Node:
    '''docstring'''

    def __init__(self, data=None, position=None):
        '''docstring'''
        self._data = data
        self._position = position
        self._pos = self._position

    @property
    def data(self):
        return self._data

    @property
    def position(self):
        return self._position


class Edge:
    '''docstring'''

    def __init__(self, nodeA=None, nodeB=None, data=None):
        '''docstring'''
        self._value = (nodeA, nodeB)
        self._nodeA = self._value[0]
        self._nodeB = self._value[1]
        self._data = data

    @property
    def value(self):
        return self._value
