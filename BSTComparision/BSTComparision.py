



def compareBST(arr1, arr2):

    print(f'arr1 {arr1}')

    print(f'arr2 {arr2}')

    if len(arr1) == 0 and len(arr2) == 0:
        return True
    

    if not arr1[0] == arr2[0]:
        return False


    if len(arr1) != len(arr2):
        return False

    root1 = arr1[0]
    root2 = arr1[0]

    arr1 = arr1[1:]
    arr2 = arr2[1:]
    arr1LeftSubTree = [a for a in  arr1 if a < root1]
    arr2LeftSubTree = [a for a in  arr2 if a < root2]
    arr1RightSubTree = [a for a in  arr1 if a >= root1]
    arr2RightSubTree = [a for a in  arr2 if a >= root2]

    return compareBST(arr1LeftSubTree, arr2LeftSubTree) and compareBST(arr1RightSubTree, arr2RightSubTree)


print(compareBST([10,15,8,12,94,81,5,2,11], [10,8,5,15,2,12,11,94,81]))