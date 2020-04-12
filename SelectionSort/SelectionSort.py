
def selection_sort(input_array):
    
    for i in range(0, len(input_array)-1):
        index = None
        smallest_number = float('inf')
        for j in range(i, len(input_array)):
            if (input_array[j] < smallest_number):
                smallest_number = input_array[j]
                index = j
        swap(input_array, i, index)
        print(input_array)
    return input_array


def swap(input_array, i, j):
    input_array[i], input_array[j] = input_array[j], input_array[i]
    return



# print(selection_sort([56,88,92,41,-62,-52,41,63,-25,-26,-52,46]))

print(selection_sort([56, 34, 91, 72, 28]))