# pylint: disable=C0103
'''CWALLE EXAMPLES'''


class Node(object):
    '''node'''

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.parent = None
        self.f = 0
        self.g = 0
        self.h = 0
        self.neighbors = []

    def __str__(self):
        '''overload string for print'''
        return "Name: " + self.name + "\nPosition: " + str(self.x) + "," + str(self.y)


def retrace(start, destination):
    '''retrace the path'''
    path = []
    current = start
    while current != destination:
        path.append(current)
        current = current.parent
        if current == destination:
            path.append(destination)
    return path


def printpath(path):
    '''print the path'''
    for i in path:
        print 'Node: ', i.name


def get_neighbors(current, nodes):
    '''get the neighbors    nodes the list of nodes to check    current the node to check nodes with'''
    # directions
    '''put those in a list'''
    '''loop over that list'''
    '''make a tuple that represents the node as a direction'''
    # example bob = Node("bob", 1, 2)
    #(1,2) != bob
    #(1,2) == (bob.x, bob.y)
    #if we get an equality then add the actual node to the neighbors list


def main():
    '''main'''
    a = Node('a', 0, 0)
    b = Node('b', 1, 0)
    c = Node('c', 1, 1)
    d = Node('d', 0, 1)
    e = Node('e', 2, 0)
    nodes = [a, b, c, d, e]
    neighbors = get_neighbors(a, nodes)
    test1 = [b, c, d]  # tests to see if equality
    testing = False
    if testing:
        # test a
        tests = [test1]
        i = 0
        for test in tests:
            if neighbors == test:
                success = True
                print 'pass', "test ", i
            else:
                success = False
                print 'fail', "test ", i
            i = i + 1

    a.neighbors = neighbors
    for i in a.neighbors:
        print i


if __name__ == '__main__':

    main()
