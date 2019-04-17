'''astar.py'''

class Node:
    def __init__(self, x, y):
        self.g = 0
        self.h = 0
        self.f = 0
        self.camefrom = None
        self.position = (x, y) #set this up into the node for now steffan will proabably ask why,
        #we can make a class that will handle positional mapping of nodes as they are created

def get_neighbors(node):
    neighbors = []
    return neighbors

def reconstruct_path(nodeA, nodeB):
    return []

def dist_between(nodeA, nodeB):
    return 10

def manhattan_distance(nodeA, nodeB):
    return 10



def astar(start, goal, heuristic):
    openSet = [start]
    closedSet= []    
    start.f_score = heuristic(start, goal)
    while openSet:
        current = openSet[0]
        if current == goal:
            return reconstruct_path(current, start)        
        for neighbor in get_neighbors(current):
            if neighbor in closedSet:
                continue

            tentative_g = current.g + dist_between(current, neighbor)

            if neighbor not in openSet:
                openSet.append(neighbor)
            else:
                if tentative_g < neighbor.g:
                    neighbor.camefrom = current
                    neighbor.g = tentative_g
                    neighbor.f = neighbor.g + heuristic(neighbor, goal)

nodes = []
for i in range(0, 4):
    for j in range(0, 4):
        nodes.append(Node(i,j))

astar(nodes[0], nodes[4], manhattan_distance)
