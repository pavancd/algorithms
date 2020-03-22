

def three_largest_numbers(input_array):
    three_largest_numbers = [float('-inf'), float('-inf'), float('-inf')]

    for n in input_array:
        if n > three_largest_numbers[0]:
            three_largest_numbers[0] = n

            if n > three_largest_numbers[1]:
                temp = three_largest_numbers[1]
                three_largest_numbers[1] = n
                three_largest_numbers[0]= temp

                if n > three_largest_numbers[2]:
                    temp = three_largest_numbers[2]
                    three_largest_numbers[2] = n
                    three_largest_numbers[1]= temp
    return three_largest_numbers




print(three_largest_numbers([56,88,92,41,-62,-52,41,92,63,-25,-26,-52,46]))