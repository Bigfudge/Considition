import numpy as np
try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

class Node:
    def __init__(self, name, heuristic):
        self.name=name
        self.neighbors= Q.PriorityQueue()
        self.weights={}
        self.heuristic=heuristic
    def setWeight(self, name, value):
        self.weights[name]=value

    def getCost(self, name):
        return self.weights[name]

    def getHeuristic(self):
        return self.heuristic

    def addNeighbor(self, newNeighbor, weight):
        name= newNeighbor.name
        self.neighbors.put(newNeighbor, weight)
        self.weights[name]=weight

    def getNearestNeighbor(self):
        return self.neighbors.get()

    def getAllNeighbors(self):
        return self.neighbors

    # def __cmp__(self, other):
    #     name=other.name
    #     return (self.cost + self.heuristic)-(other.getCost(name) + other.getHeuristic(name))

class Grapf(object):
    def __init__(self):
        self.nodes = {}
        self.frontier = Q.PriorityQueue()
        self.currentNode = 0
        self.cameFrom= {}
        self.costSoFar= {}

    def addNode(self, newNode):
        name = newNode.name
        self.nodes[name]=newNode


def Astar(start, end, graph):
    came_from= {}
    cost_so_far= {}
    graph.frontier.put(start,0)
    came_from[start.name] = None
    cost_so_far[start.name] = 0

    while not graph.frontier.empty():
        graph.currentNode = graph.frontier.get()

        if graph.currentNode.name == end.name:
            print('BREAK')
            break

        currentNeighbors= graph.currentNode.getAllNeighbors()
        for next in currentNeighbors.queue:
            new_cost = cost_so_far[graph.currentNode.name] + graph.currentNode.getCost(next.name)

            # print('New Cost', new_cost)
            print('Name:', next.name, 'Value:', new_cost)
            print('Cost so far:', cost_so_far)

            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next.name] = new_cost
                priority = new_cost + next.getHeuristic()
                graph.frontier.put(next, priority)
                came_from[next.name] = graph.currentNode

    return came_from, cost_so_far


def main():
    n1 = Node('Start',0)
    n2 = Node('node2',0)
    n3 = Node('node3',0)
    n4 = Node('node4',0)
    n5 = Node('Goal',0)

    n1.addNeighbor(n2,1)
    n1.addNeighbor(n3,1)
    n2.addNeighbor(n4,1)
    n3.addNeighbor(n5,5)
    n4.addNeighbor(n5,6)

    g = Grapf()
    g.addNode(n1)
    g.addNode(n2)
    g.addNode(n3)
    g.addNode(n4)
    g.addNode(n5)

    came_from, cost_so_far = Astar(n1, n5, g)

    #print(came_from)
    print(cost_so_far)


main()
