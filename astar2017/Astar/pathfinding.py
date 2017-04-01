'''pathfinding.py'''
import math


class Node(object):
    '''node'''

    def __init__(self, guid, data):
        '''init'''
        self.guid = guid
        self.data = data

    def __str__(self):
        '''str'''
        return str.format('({0}{1}) ', self.data.pos[0], self.data.pos[1])


class Data(object):
    '''data'''

    def __init__(self, position):
        '''init'''
        self.pos = position
        self.h = 0
        self.g = 0
        self.f = self.h + self.g
        self.walkable = True
        self.neighbors = []
        self.parent = None

    def __getitem__(self, key):
        return self.pos[key]

    def __str__(self):
        '''str'''
        return str.format('{0} ({1},{2}) ', 'pos', self.pos[0], self.pos[1])


def manhattan(start, goal):
    '''mhd'''

    ydif = abs(goal.data[1] - start.data[1])
    xdif = abs(goal.data[0] - start.data[0])

    return xdif + ydif


def costtomove(start, goal):
    '''ctm'''
    if start.data[0] == goal.data[0] or start.data[1] == goal.data[1]:
        return 10
    return 14


def getneighbors(node, nodes):
    '''asdf'''
    current = node.data
    right = (current[0] + 1, current[1])
    top_right = (current[0] + 1, current[1] + 1)
    top = (current[0], current[1] + 1)
    top_left = (current[0] - 1, current[1] + 1)
    left = (current[0] - 1, current[1])
    bottom_left = (current[0] - 1, current[1] - 1)
    bottom = (current[0], current[1] - 1)
    bottom_right = (current[0] + 1, current[1] - 1)
    directions = [right, top_right, top, top_left,
                  left, bottom_left, bottom, bottom_right]
    neighbors = []
    for i in nodes:
        node = (i.data[0], i.data[1])
        if node in directions:
            neighbors.append(i)
    return neighbors


def retrace(goal):
    '''retrace'''
    current = goal
    path = []
    path.append(current.data)
    while current.data.parent != None:
        current = current.data.parent
        path.append(current.data)

    return path


def astar(start, goal, graph):
    '''astar'''
    openlist = []
    closedlist = []
    path = []
    openlist.append(start)
    openlist.sort(key=lambda x: x.data.f)

    while openlist:
        current = openlist[0]
        openlist.remove(current)
        closedlist.append(current)
        if goal in openlist:
            path = retrace(current)
        neighbors = getneighbors(current, graph)
        for nay in neighbors:
            if nay in closedlist or not nay.walkable:
                continue
            tentative_g = nay.data.g + costtomove(current, nay)
            if nay not in openlist:
                openlist.append(nay)
            elif tentative_g >= nay.data.g:
                continue
            nay.data.parent = current
            nay.data.g = tentative_g
            nay.data.h = manhattan(nay, goal)
            nay.data.f = nay.data.g + nay.data.h

    return path


def main():
    '''main'''
    graph = []
    count = 0
    for ypos in range(10):
        for xpos in range(10):
            dat = Data((xpos, ypos))
            graph.append(Node(str(count), dat))
        count += 1
    count = 1
    for i in graph:
        if count % 10 == 0:
            print i, '\n'
        else:
            print i,
        count += 1

    start = graph[0]
    nays = getneighbors(start, graph)
    print 'neighbors for ', start.guid, '@', start
    for i in nays:
        print i,
    print '\n'
    print 'manhattan test', graph[0], graph[99], manhattan(graph[0], graph[99])

    goal = graph[99]
    result = astar(start, goal, graph)
    count = 1
    for i in graph:
        if count % 10 == 0:
            print i, '\n'
        elif i.data in result:
            print '(->)',
        else:
            print i,
        count += 1



if __name__ == '__main__':
    main()
