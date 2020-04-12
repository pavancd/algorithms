def max_sum_substring(input):
    
    max_sum_ending_here = input[0]
    max_sum_so_far = input[0]

    for i in range(1, len(input)):
        max_sum_ending_here = max(input[i], input[i]+max_sum_ending_here)
        max_sum_so_far = max(max_sum_so_far, max_sum_ending_here)

    return max_sum_so_far


print(max_sum_substring([1, 5, 4, -8, 6, 9, -5])) 