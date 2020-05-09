def zigZagTraverse(matrix):
    print(matrix[0][0])

    r = 1
    c = 0

    while r != len(matrix[0]) and c != len(matrix):
        if r == len(matrix) - 1 or c == 0:
            r, c = traverseDiagonallyUp(r, c, matrix)
            
        elif r == 0 or c == len(matrix[0]) - 1:
            r, c = traverseDiagonallyDown(r, c, matrix)
        
        if  r == len(matrix[0])-1 and c == len(matrix)-1:
            print(matrix[r][c])
            break



def traverseDiagonallyUp(r, c, matrix):
    while r > 0 and c < len(matrix[0]) - 1:
        print(matrix[r][c])

        r -= 1
        c += 1
    if r == len(matrix[0])-1 and c == len(matrix)-1:
        return r , c

    if c == len(matrix[0]) - 1:
        print(matrix[r][c])
        r, c = r+1 , c
        # print(matrix[r][c])
        return r, c 
    elif r == 0:
        print(matrix[r][c])
        r, c = 0, c+1
        # print(matrix[r][c])
        return r, c 
    
    



def traverseDiagonallyDown(r, c, matrix):
    while r < len(matrix) - 1 and c > 0 :
        print(matrix[r][c])

        r += 1
        c -= 1
        
    if r == len(matrix[0])-1 and c == len(matrix)-1:
        return r , c

    if c == 0:
        print(matrix[r][c])
        r, c =  r+1 , c
        # print(matrix[r][c])
        return r, c 

    elif r ==  len(matrix) - 1:
        print(matrix[r][c])
        r, c = r, c+1
        # print(matrix[r][c])
        return r, c 
    
    





r1 = [1, 3,  4,  10]
r2 = [2, 5,  9,  11]
r3 = [6, 8, 12,  15]
r4 = [7, 13, 14, 16]

zigZagTraverse([r1, r2, r3, r4])