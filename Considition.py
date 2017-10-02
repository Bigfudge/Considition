import numpy as np
try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

class Node:
    def __init__(self, name, cost, heuristic):
        self.name=name
        self.neighbors= Q.PriorityQueue()
        self.cost= cost;
        self.heuristic=heuristic;
    def setCost(self, value):
        self.cost=value

    def setHeuristic(self, value):
        self.heuristic=value

    def getName(self):
        return self.name

    def getCost(self):
        return self.cost

    def getHeuristic(self):
        return self.heuristic

    def addNeighbor(self, newNeighbor):
        self.neighbors.put(newNeighbor)

    def getNearestNeighbor(self):
        return self.neighbors.get()

    def getAllNeighbors(self):
        return self.neighbors

    def __cmp__(self, other):
        return (self.cost + self.heuristic)-(other.getCost() + other.getHeuristic())

class Grapf(object):
    def __init__(self):
        self.nodes = Q.PriorityQueue()
        self.frontier = Q.PriorityQueue()
        self.currentNode = 0
        self.cameFrom= {}
        self.costSoFar= {}
    
    def addNode(self, newNode):
        seld.nodes.put(newNode)

    def Astar(start, end):
        self.frontier.put(start)
        self.came_from[start] = None
        self.cost_so_far[start] = 0

        while not frontier.empty():
            self.currentNode = self.frontier.get()

            if self.currentNode == end:
                break
            frontier.put(currentNode.getAllNeighbors())
            for i in range(len(frontier)):






n1 = Node('node1',10, 0)
n2 = Node('node2', 5, 0)
n3 = Node('node3', 6, 0)

n1.addNeighbor(n2)
n1.addNeighbor(n3)

test= n1.getNearestNeighbor().name
print(test)
