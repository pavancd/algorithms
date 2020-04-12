class Node:
    def __init__(self, name):
        self.name = name
        self.children = []


    def addChild(self, name):
        self.children.append(name)


    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)

        return array

    def breadthFirstSearch(self, array=[]):
      container = [self]

      while len(container) > 0:
        el = container.pop(0)
        array.append(el.name)
        for e in el.children:
            container.append(e)

      return array

nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')
nodeE = Node('E')
nodeF = Node('F')
nodeG = Node('G')
nodeA.children = [nodeB, nodeC]
nodeB.children = [nodeD, nodeE]
nodeC.children = [nodeF, nodeG]

print(nodeA.breadthFirstSearch())


# array = [1,2,3,4,6]

# print(array.pop())
# print(array)

