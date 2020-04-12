def singleCycle(input):
  currentIdx = 0
  numberOfSteps = 0

  while numberOfSteps < len(input):
    if numberOfSteps > 0 and currentIdx == 0:
      return False

    currentIdx = getNextIndex(currentIdx, input)
    numberOfSteps += 1

  return currentIdx == 0


def getNextIndex(currentIdx, array):
  jump = array[currentIdx]

  nextIdx = (currentIdx + jump) % len(array)

  return nextIdx if nextIdx >=0 else len(array)+nextIdx


print(singleCycle([2, 3, 1, -4, -3, 2]))