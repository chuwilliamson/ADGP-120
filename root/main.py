'''main.py'''
from graphrenderer.game import Game
from graphrenderer.gameObject import GameObject
from graphrenderer.graphObject import GraphObject
from graphrenderer.lineObject import LineObject
#imports are in the form of folder.file import class
from root.graphdata.graph import Graph,Node,Edge

from utilities.freefunctions import run
from steering.agent import Agent


def doit():
    '''main execution func'''
    g = Game("game")    
    n1 = Node(1, (200, 200))
    n2 = Node(2, (200, 500))
    n3 = Node(3, (500, 500))
    n4 = Node(4, (500, 200))
    nodes = [n1, n2, n3, n4]
    edges = [Edge(n1,n2), Edge(n2,n3), Edge(n2,n4), Edge(n3, n1)]    
    graph = Graph(nodes, edges) 
    
    for node,line in zip(graph.Nodes, graph.Edges):
        n = GraphObject(node._data, node._pos)
        l = LineObject(1, (line._nodeA, line._nodeB))
        g.gameObjects.extend((n, l))

def main():
    g = Game("steering")    
    g.gameObjects.append(Agent((100, 100),(1, 1), GraphObject(None, [100, 100])))
    run(g)

main()