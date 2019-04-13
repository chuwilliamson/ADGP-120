'''main.py'''
from pygame import *
from graphrenderer.game import *
from graphrenderer.graphObject import *
from graphrenderer.lineObject import *
from graphdata.graph import *
from constants import *


def main():
    '''main execution func'''
    game = Game("game")

    # Set 'chart' below to your instance of a graph.
    # A 'graph' takes in two parameters: Graph(nodes_list, edges_list)

    node1 = Node(1, (200, 200))
    node2 = Node(2, (200, 500))
    node3 = Node(3, (500, 500))
    node4 = Node(4, (500, 200))
    nodes = [node1, node2, node3, node4]

    edges = [Edge(node1, node2), Edge(node2, node3), Edge(node2, node4),
             Edge(node3, node1)]

    chart = Graph(nodes, edges)

    nodeobjects = []
    lineobjects = []
    for node, edge in zip(chart.nodes, chart.edges):
        nodeobjects.append(GraphObject(node.data, node.position))
        lineobjects.append(LineObject(1, (edge.value[0], edge.value[1])))

    for node, line in zip(nodeobjects, lineobjects):
        game.add_gameobject(node, line)

    # add the gameObjects here
    if game._startup():  # if the game starts up correctly
        while game._update():  # update the game if the game updates then
            game._draw()  # draw elements from the game
        game._shutdown()


main()
