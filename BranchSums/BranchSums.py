
class BinaryTree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def add(self, value):
        pass


def BranchSums(root):
    sums = []
    calculateBranchSum(root, sums, 0)
    return sums


def calculateBranchSum(root, sums, runningSum):
    if root is None:
        return
    newRunningSum = runningSum + root.value

    if root.left == None and root.right == None:
        sums.append(newRunningSum)
        return 

    calculateBranchSum(root.left, sums, newRunningSum)
    calculateBranchSum(root.right, sums, newRunningSum)


def test():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)


    sums = BranchSums(root)
    print(sums)


test()