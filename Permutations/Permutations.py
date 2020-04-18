# #O(n!*n*n)  | O(n*n!)
# def getPermutations(array):
#     permutations = []
#     permutationHelper(array, [], permutations)
#     return permutations


# def permutationHelper(array, currentPermution, permutations):
#     if not len(array) and len(currentPermution):
#         permutations.append(currentPermution)
 
#     else:
#         for i in range(len(array)):
#             newArray = array[:i] +  array[i+1:]
#             newPermutation = currentPermution + [array[i]]
#             permutationHelper(newArray, newPermutation, permutations)




# second approach
def getPermutations(array):
    permutations = []
    permutationHelper(0, array, permutations)
    return permutations


def permutationHelper(i, array, permutations):
    if i == len(array)-1:
        permutations.append(array[:])
 
    else:
        for j in range(i, len(array)):
            swap(array, i, j)
            permutationHelper(i+1, array, permutations)
            swap(array, i, j)

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


matrix = getPermutations([1, 2, 3])
print(len(matrix))
print(matrix)
