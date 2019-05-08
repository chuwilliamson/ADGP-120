'''astar.py'''
'''Matthew Williamson 2019'''
DIMS = 4


class Node:
    def __init__(self, id_=None, value=None):
        self.id = id_
        self.g = 0
        self.h = 0
        self.f = 0
        self.value = value
        self.camefrom = None
        # set this up into the node for now steffan will proabably ask why,
        # we can make a class that will handle positional mapping of nodes as they are created

    def __str__(self):
        return str.format("Node: %s " % self.id)

def is_neighbor(nodeA, nodeB, graph = None):
    right = nodeA.id + 1
    up = nodeA.id + DIMS
    left = nodeA.id - 1
    down = nodeA.id - DIMS

    cardinals = [right, up, left, down]  # up down left and right
    # use the up down left and right
    diagonals = [up + 1, up - 1, down + 1, down - 1]

    return nodeB in cardinals or nodeB in diagonals

def dist_between(nodeA, nodeB, graph=None):
    ''' calculate the distance between two nodes'''
    result = 0

    right = nodeA.id + 1
    up = nodeA.id + DIMS
    left = nodeA.id - 1
    down = nodeA.id - DIMS

    cardinals = [right, up, left, down]  # up down left and right
    # use the up down left and right
    diagonals = [up + 1, up - 1, down + 1, down - 1]

    for d in diagonals:
        notdiagonal = d % 4 == 0 or d < 0
        if notdiagonal:
            diagonals.remove(d)

    if nodeB.id in cardinals:
        result = 10
    if nodeB.id in diagonals:
        result = 14
    return result

def get_neighbors(node, graph=None):
    '''get neighbors of a node'''
    '''giving it this way will cause the students to wonder how to do this without knowing what list it is in'''
    '''this is a global function that could reference global variables'''
    '''or call a function that does know the neighbor list'''
    neighbors = []
    for n in graph:
        if dist_between(node, n) not in (10, 14):
            continue
        neighbors.append(n)
    return neighbors


def manhattan_distance(nodeA, nodeB, graph=None):
    return 10


def reconstruct_path(nodeA, nodeB):
    current = nodeB
    result = []
    while current.parent != None:
        current = current.parent
    return result


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
                nodes_.append(Node(id_=str.format("%s, (%s,%s)"% (count,i,j)), value=(i, j)))
                count += 1
        self.nodes = nodes_

    def test(self):
        f = open("testdistance.txt", mode='w')
        f.write(test_distance(self.nodes))
        f.close()

        f = open("testneighbors.txt", mode='w')
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
                counterstr = "0" + str(counter)
            valstr += counterstr + '|'
            if j == DIMS-1:
                valstr += '\n'
            counter += 1
    return valstr


def test_distance(nodes):  # done
    resultstr = ''
    for i in nodes:
        resultstr += str(i) + "\n"
        for j in nodes:
            resultstr += str.format(" distance to %s == %s \n" %
                                    (j, dist_between(i, j)))
        resultstr += "===========================\n"
    return resultstr


def test_neighbors(nodes):
    resultstr = ''
    for i in nodes:
        resultstr += str(i) + "\n"
        neighbors = get_neighbors(i, nodes)
        resultstr += "neighbors: " + str_list(neighbors)
        resultstr += "\n===========================\n"
    return resultstr


p = Program()
p.run()
p.test()

'''
00 01 02 03
04 05 06 07
08 09 10 11
12 13 14 15

00 => 01, 04, 05
01 => 02, 00, 04, 05, 06
'''
