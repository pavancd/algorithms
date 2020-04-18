# 1   0   0   1   0
# 1   0   1   0   0   
# 0   0   1   0   1
# 0   0   1   0   1
# 0   0   1   1   0


def riverSize(matrix):
    riverSizes = []

    visited = [ [False for value in row ] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if visited[i][j]:
                continue
            if matrix[i][j] == 0:
                visited[i][j] = True
                continue
            
            currentRiverSize = traverseRiver(matrix, visited, i, j)
            if currentRiverSize > 0: 
                riverSizes.append(currentRiverSize)

    return riverSizes


def traverseRiver(matrix, visited, i, j):
    riverSize = 0
    stack = [[i, j]]

    while len(stack) != 0:
        node = stack.pop()
        rowIdx = node[0]
        colIdx = node[1]

        if visited[rowIdx][colIdx]:
            continue

        visited[rowIdx][colIdx] = True
        if matrix[rowIdx][colIdx] == 0:
            continue
            
        riverSize += 1
        unvisitedNeighbouringNodes = getUnvisitedNeighbouringNodes(matrix, visited, rowIdx, colIdx)
        for n in unvisitedNeighbouringNodes:
            stack.append(n)

    return riverSize


def getUnvisitedNeighbouringNodes(matrix, visited, i, j):
    unvisitedNeighbouringNodes = []

    if i > 0 and not visited[i-1][j]:
        unvisitedNeighbouringNodes.append([i-1, j])

    if i < len(matrix) - 1 and not visited[i+1][j]:
        unvisitedNeighbouringNodes.append([i+1, j])

    if j > 0 and not visited[i][j-1]:
        unvisitedNeighbouringNodes.append([i, j-1])

    if j < len(matrix[i]) - 1 and not visited[i][j+1]:
        unvisitedNeighbouringNodes.append([i, j+1])

    return unvisitedNeighbouringNodes

row1 = [1, 0, 0, 1, 0]
row2 = [1, 0, 1, 0, 0]
row3 = [0, 0, 1, 1, 1]
row4 = [0, 0, 1, 0, 1]
row5 = [0, 0, 1, 1, 1]


matrix = [row1, row2, row3, row4, row5]
riverSizes = riverSize(matrix)
print('-'*10 + 'Rivers array' + '-'*10)
print(riverSizes)
print('-'*10 + 'Longest river' + '-'*10)
print(max(riverSizes))