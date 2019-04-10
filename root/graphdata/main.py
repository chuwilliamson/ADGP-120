from root.graphrenderer.game import *
from root.graphrenderer.gameObject import *
from root.graphrenderer.graphObject import *
from root.graphrenderer.lineObject import *

from root.graphdata.graph import *


def main():
    '''main execution func'''
    game = Game("game")

    ''' #To Test the graph renderer, uncomment the following code
    n1 = graph.Node(1, (200, 200))
    n2 = graph.Node(2, (200, 500))
    n3 = graph.Node(3, (500, 500))
    n4 = graph.Node(4, (500, 200))
    node_list = [n1, n2, n3, n4]

    e1 = graph.Edge(n1, n2)
    e2 = graph.Edge(n2, n3)
    e3 = graph.Edge(n2, n4)
    edge_list = [e1, e2, e3]
    '''
    ### Set 'chart' below to your instance of a graph.
    ### A 'graph' takes in two parameters: Graph(nodes_list, edges_list)
    
    n1 = Node(1, (200, 200))
    n2 = Node(2, (200, 500))
    n3 = Node(3, (500, 500))
    n4 = Node(4, (500, 200))
    nodes = [n1, n2, n3, n4]

    edges = [Edge(n1,n2), Edge(n2,n3), Edge(n2,n4), Edge(n3, n1)]
    
    chart = Graph(nodes, edges) 
    
    nodeobjects = []
    lineobjects = []
    for node,line in zip(chart.Nodes, chart.Edges):
        nodeobjects.append(GraphObject(node._data, node._pos))
        lineobjects.append(LineObject(1, (line._nodeA, line._nodeB)))
 
    for n,l in zip(nodeobjects, lineobjects):
        game.gameObjects.append(n)
        game.gameObjects.append(l)
        
        

    #add the gameObjects here
    if game._startup():#if the game starts up correctly
        while game._update():#update the game if the game updates then
            game._draw()#draw elements from the game
        game._shutdown()

main()

