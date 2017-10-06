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
        self.nodes.put(newNode)
    def getCost(a, b):
        

def Astar(start, end, graph):
    came_from= {}
    cost_so_far= {}
    graph.frontier.put(start)
    came_from[start.name] = None
    cost_so_far[start.name] = 0

    while not graph.frontier.empty():
        graph.currentNode = graph.frontier.get()
        print(graph.currentNode.name)

        if graph.currentNode.name == end.name:
            break
        print(graph.currentNode.name)

        currentNeighbors= graph.currentNode.getAllNeighbors()

        for next in currentNeighbors.queue:
            new_cost = cost_so_far[currentNode.name] + graph.getCost(currentNode, next)

            print(new_cost)

        if next not in cost_so_far or new_cost < cost_so_far[next]:
            cost_so_far[next.name] = new_cost
            priority = new_cost + graph.getHeuristic(end, next)
            frontier.put(next, priority)
            came_from[next.name] = current

        return costSoFar


def main():
    n1 = Node('Start',1, 0)
    n2 = Node('node2',5, 0)
    n3 = Node('node3',6, 0)
    n4 = Node('node4',2, 0)
    n5 = Node('Goal',1, 0)

    n1.addNeighbor(n2)
    n1.addNeighbor(n3)
    n2.addNeighbor(n4)
    n3.addNeighbor(n5)
    n4.addNeighbor(n5)

    g = Grapf()
    g.addNode(n1)
    g.addNode(n2)
    g.addNode(n3)
    g.addNode(n4)
    g.addNode(n5)

    costTot = Astar(n1, n5, g)

    print(costTot)


main()
