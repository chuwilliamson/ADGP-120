'''graph.py'''

from node import Node


class Graph(object):
    '''graph object'''
    def __init__(self, vertices=None, edges=None):
        '''create square graph'''
        self._nodes = {}
        for node in vertices:
            self._nodes[node.identifier] = node
        self._edges = edges

    def get_node(self, node):
        '''get a node by it's identifier'''
        if node in self._nodes:
            return self._nodes[node]
        else:
            print node, "is not in dictionary"

    @property
    def get_names(self):
        '''get all names of nodes in graph'''
        return self._nodes.keys

    @property
    def get_nodevalues(self):
        '''get all the nodes'''
        return self._nodes.items

    def set_neighbors(self, node, graph):
        '''get neighbors for a node'''
        neighbors = []
        dirs = [
            [1, 0], [1, 1], [0, 1], [-1, 1],
            [-1, 0], [-1, -1], [0, -1], [1, -1]
            ]

        for i in dirs:
            item1 = i[0] + node.value[0]
            item2 = i[1] + node.value[1]
            fetch_node = graph.get_node((str(item1), str(item2)))
            if fetch_node:
                neighbors.append(fetch_node.identifier)
        return neighbors


def test_graph():
    '''abc'''
    nodes = []
    name = 65
    for i in range(5):
        for j in range(5):
            nodes.append(Node(chr(name), (i, j)))
            name += 1
    graph = Graph(nodes)
    node = graph.get_node('A')
    print node
    print graph.get_names()
    # neighbors = get_neighbors(node, graph)
    # for neighbor in neighbors:
    #     print neighbor

if __name__ == "__main__":
    test_graph()
