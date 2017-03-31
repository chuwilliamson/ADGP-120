'''testing.py'''


class Tester(object):
    '''testing class'''

    def test(self, functiontotest):
        '''yes'''
        expectedoutput = [None]
        start = None
        goal = None
        if functiontotest(start, goal) == expectedoutput:
            print 'pass'
            return True
        else:
            print 'fail'
            return False
        # new configuratjion
        expectedoutput = [4, 3, 2, 1]
        start = 1
        goal = 4
        if functiontotest(start, goal) == expectedoutput:
            print 'pass'
            return True
        else:
            print 'fail'
            return False


def astar(start, destination):
    '''dummy algo'''
    path = []
    current = start
    while current != destination:
        path.append(current)
        previous = current
        current.parent = previous
    if current == destination:
        path.append(destination)
        return path

    return [None]


def main():
    '''main'''
    tester = Tester()
    tester.test(astar)


if __name__ == '__main__':
    main()
