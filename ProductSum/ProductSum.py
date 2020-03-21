

def product_sum(inputArray, multiplier=0):
    sum = 0
    multiplier += 1
    for el in inputArray:
        if isinstance(el, list):
            sum += product_sum(el, multiplier)
        else:
            sum += el
    return sum * multiplier





print(product_sum([5, 2, [7,-1], 3, [ 6, [ -13, 8], 4]]))

# print(isinstance([1,2,3], list))