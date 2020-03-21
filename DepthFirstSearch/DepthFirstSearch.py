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

node = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')
nodeE = Node('E')
nodeF = Node('F')
nodeG = Node('G')
node.children = [nodeB, nodeC]
nodeB.children = [nodeD, nodeE]
nodeC.children = [nodeF, nodeG]

print(node.depthFirstSearch([]))



