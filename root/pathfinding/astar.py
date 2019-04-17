'''astar.py'''
'''Matthew Williamson 2019'''
DIMS = 4
class Node:
    def __init__(self, id=None, value=None):
        self.id = id
        self.g = 0
        self.h = 0
        self.f = 0
        self.camefrom = None
        # set this up into the node for now steffan will proabably ask why,
        # we can make a class that will handle positional mapping of nodes as they are created

    def __str__(self):
        return str.format("Node: %s " % self.id)

def dist_between(nodeA, nodeB, graph=None):
    ''' calculate the distance between two nodes'''
    if nodeB.id - nodeA.id not in (1, 4):
        return 0
    if nodeA == nodeB:
        return 0    
    cardinals = [nodeA.id + 1, nodeA.id - 1, nodeA.id + DIMS, nodeA.id - DIMS]   
    
    if nodeB.id in cardinals:
        return 10    
    return 14

def get_neighbors(node, graph=None):
    '''get neighbors of a node'''
    '''giving it this way will cause the students to wonder how to do this without knowing what list it is in'''
    '''this is a global function that could reference global variables'''
    '''or call a function that does know the neighbor list'''
    neighbors = []
    for n in graph:        
        if dist_between(node, n) == 0:
            continue
        neighbors.append(n)
    return neighbors

def manhattan_distance(nodeA, nodeB, graph=None):
    return 10


def reconstruct_path(nodeA, nodeB):
    return []


def astar(start, goal, heuristic):
    openSet = [start]
    closedSet = []
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
class Program:
    def __init__(self):
        self.nodes = []
        self.count = 0
    def run(self):
        nodes_ = []
        count = 0
        for i in range(0, DIMS):
            for j in range(0, DIMS):
                nodes_.append(Node(id=count, value=(i, j)))
                count += 1
        self.nodes = nodes_

    def test(self):
        f = open("testdistance.txt", mode= 'w')    
        f.write(test_distance(self.nodes))
        f.close()

        f = open("testneighbors.txt", mode = 'w')
        f.write(test_neighbors(self.nodes))
        f.close()
        

def printgrid(nodes):
    valstr = ''
    counter = 0
    for i in range(0, DIMS):
        valstr += '|'
        for j in range(0, DIMS):
            counterstr = str(counter)
            if counter <= 9:
                counterstr="0" + str(counter)
            valstr+= counterstr + '|'
            if j== DIMS-1:
                valstr+= '\n'
            counter += 1
    return valstr

def test_distance(nodes):#done    
    resultstr = ''
    for i in nodes:
        resultstr += str(i) + "\n"         
        for j in nodes:                        
            resultstr += str.format(" distance to %s == %s \n" % (j, dist_between(i, j)))            
        resultstr+= "===========================\n"
    return resultstr
def str_list(items):
    result = ""
    for i in items:
        result+= str(i) + ""
    return result

def test_neighbors(nodes):
    resultstr = ''
    for i in nodes:
        resultstr += str(i) + "\n"              
        neighbors = get_neighbors(i, nodes)                        
        resultstr += "neighbors: " + str_list(neighbors)
        resultstr+= "\n===========================\n"
    return resultstr
       



#astar(nodes[0], nodes[4], manhattan_distance)