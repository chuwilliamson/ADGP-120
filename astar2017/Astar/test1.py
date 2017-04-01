'''Hello World.'''
import math


def retrace(start, endnode):
    """Retracing path from goal to start."""
    path = []
    itera = endnode
    while itera is not start:
        path.append(itera)
        itera = itera.parent
    return path


def dist(current, anext):
    """Estimates the distance."""
    return 10 if current[0] == anext[0] or current[1] == anext[1] else 14


def mhdm(nodetotest, goal):
    """need documentation"""
    x = abs(goal[0] - nodetotest[0])
    y = abs(goal[1] - nodetotest[1])
    if x > y:
        return (y * 14) + (x - y) * 10
    if y > x:
        return (x * 14) + (y - x) * 10
    else:
        return x * 14


def mhd(nodetotest, goal):
    """need documentation"""
    return (abs(goal[0] - nodetotest[0]) + abs(goal[1] - nodetotest[1])) * 10


def astar(start, goal, graph):
    """need documentation"""
    camefrom = []
    closed = []
    open = []
    start.h = 0
    start.g = 0
    start.f = start.g + start.h
    open.append(start)
    while len(open) != 0:
        open = sorted(open, key=lambda x: x.f)
        current = open[0]
        open.remove(current)
        closed.append(current)
        if current == goal:
            camefrom = retrace(start, current)
            return camefrom
        for nay in getneighbors(current, graph):
            if nay in closed or nay.walkable is False:
                continue
            tentative_g = current.g + dist(current, nay)
            if nay not in open:
                open.append(nay)
            elif tentative_g >= nay.g:
                continue
            nay.parent = current
            nay.g = tentative_g
            nay.h = mhdm(nay, goal)
            nay.f = nay.g + nay.h
    return camefrom

import pathfinding
from pathfinding import testfunc
from pathfinding import getneighbors



def main():
   # for _ in range(10):
        #testfunc(astar)
    failcount = 0
    passcount = 0
    for _ in range(1000):
        res = testfunc(astar)
        if res:
            passcount += 1
        else:
            failcount += 1
    print str.format('fails {0}, passes {1}', failcount, passcount)


if __name__ == '__main__':
    main()
