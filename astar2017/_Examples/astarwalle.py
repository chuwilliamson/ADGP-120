from testing import Tester 


class Node(object):
    '''node'''

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.parent = None
        self.g = None
        self.h = None
        self.f = None

    def __str__(self):
        '''overload string for print'''
        return "Name: " + self.name + "\nPosition: " + str(self.x) + ", " + str(self.y)


def get_neighbors(current, nodes):
    '''get the neighbors '''
    # nodes the list of nodes to check    current the node to check nodes with'''
    # directions
    # put those in a list'''
    # loop over that list'''
    # make a tuple that represents the node as a direction'''
    # example bob = Node("bob", 1, 2)
    #(1,2) != bob
    #(1,2) == (bob.x, bob.y)
    # if we get an equality then add the actual node to the neighbors list
    right = (current.x + 1, current.y)
    top_right = (current.x + 1, current.y + 1)
    top = (current.x, current.y + 1)
    top_left = (current.x - 1, current.y + 1)
    left = (current.x - 1, current.y)
    bottom_left = (current.x - 1, current.y - 1)
    bottom = (current.x, current.y - 1)
    bottom_right = (current.x + 1, current.y - 1)
    directions = [right, top_right, top, top_left,
                  left, bottom_left, bottom, bottom_right]
    neighbors = []
    for i in nodes:
        node = (i.x, i.y)
        if node in directions:
            neighbors.append(i)
    return neighbors


def find_g(node, neighbors):
    gcosts = []
    for i in neighbors:
        xdifference = i.x - node.x
        ydifference = i.y - node.y
        totaldifference = xdifference + ydifference
        if totaldifference == 1 or totaldifference == -1:
            i.g = 10
            gcosts.append(i.g)
        else:
            i.g = 14
            gcosts.append(i.g)
    return gcosts


def find_h(neighbors, destination):
    hcosts = []
    for i in neighbors:
        xleft = destination.x - i.x
        if xleft < 1:
            xleft = xleft * -1
        yleft = destination.y - i.y
        if yleft < 1:
            yleft = yleft * -1
        totalleft = xleft + yleft
        i.h = totalleft * 10
        hcosts.append(i.h)
    return hcosts


def find_f(neighbors):
    fcosts = []
    for i in neighbors:
        i.f = i.g + i.h
        fcosts.append(i.f)
    return fcosts


def find_lowest(neighbors):
    '''get the lowest f score'''
    neighbors.sort(key=lambda x: x.f)
    return neighbors[0]


def astar(start, destination):
    path = []
    current = start
    while current != destination:
        path.append(current)
        neighbors = get_neighbors(current, nodes)
        find_g(current, neighbors)
        find_h(neighbors, destination)
        find_f(neighbors)
        next_node = find_lowest(neighbors)
        previous = current
        current = next_node
        current.parent = previous
    if current == destination:
        path.append(destination)
        return path

    return [None]


def main():
    '''main'''
    tester = Tester()
    tester.test(astar)

    # graph = []
    # index = 0
    # for y in range(10):
    #     for x in range(10):
    #         name = str(index)
    #         node = Node(name, x, y)
    #         graph.append(node)
    #         index += 1
    # openlist = []
    # closedlist = []
    # start = graph[0]
    # goal = graph[50]
    # openlist.append(start)
    # while openlist:
    #     current = openlist[0]
    #     print current
    #     openlist.remove(current)
    #     closedlist.append(current)
    #     neighbors = get_neighbors(current, graph)
    #     if goal in openlist:
    #         print 'win'
    #         break
    #     for neighbor in neighbors:
    #         if neighbor not in openlist:
    #             openlist.append(neighbor)

    # tests to see if the astar function works


if __name__ == '__main__':
    main()
