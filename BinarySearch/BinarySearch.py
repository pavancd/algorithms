

def binary_search(inputArray, target):
    
    left = 0
    right = len(inputArray)

    while left < right:
        middle = round((left+right)/2)
        if inputArray[middle] == target:
            return True
        elif inputArray[middle] > target:
            right = middle - 1
        elif inputArray[middle] < target:
            left = middle + 1
        
    return False



print(binary_search([1, 2, 3, 5, 6, 8, 9], 10))