
def insertion_sort(input_array):
    sorted_array_index = 0

    while  sorted_array_index < len(input_array) - 1:
        
        for i in reversed(range(0, sorted_array_index+1)):
            if input_array[i] > input_array[i+1]:
                swap(input_array, i, i+1)
            else:
                break

        sorted_array_index += 1
        print(input_array)
    return input_array


def swap(input_array, i, j):
    input_array[i], input_array[j] = input_array[j], input_array[i]
    return



# print(insertion_sort([56,88,92,41,-62,-52,41,92,63,-25,-26,-52,46]))

print(insertion_sort([56, 34, 91, 72, 28]))