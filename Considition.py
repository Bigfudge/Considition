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
    def addNode(self, newNode):
        seld.nodes.put(newNode)

    def Astar(start, end):
        currentNode = start
        frontier.put(currentNode)
        while not frontier.empty():
            current = frontier.get()

            if current == goal:
            break
            frontier.put(currentNode.getAllNeighbors())





n1 = Node('node1',10, 0)
n2 = Node('node2', 5, 2)
n3 = Node('node3', 6, 0)

n1.addNeighbor(n2)
n1.addNeighbor(n3)

test= n1.getNearestNeighbor().name
print(test)
