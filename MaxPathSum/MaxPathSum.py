
class BinaryTree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        pass


def maxPathSum(root):
    _, maxPathSum = findMaxPathSum(root)
    return maxPathSum


def findMaxPathSum(root):

    if root is None:
        return (0, 0)

    maxLeftSumAsBranch, maxLeftPathSum = findMaxPathSum(root.left)
    maxRightSumAsBranch, maxRightPathSum = findMaxPathSum(root.right)

    maxChildSumAsBranch = max(maxLeftSumAsBranch, maxRightSumAsBranch)

    value = root.value
    maxSumAsBranch = max(maxChildSumAsBranch + value, value)

    maxSumAsTriangle = max(
        maxSumAsBranch, maxLeftSumAsBranch + value + maxRightSumAsBranch)

    maxPathSum = max(maxSumAsTriangle, maxLeftPathSum, maxRightPathSum)

    return (maxSumAsBranch, maxSumAsTriangle)


root = None


def test():
    global root
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.left = BinaryTree(10)
    root.right.right = BinaryTree(8)


if __name__ == '__main__':
    test()
    print(maxPathSum(root))
