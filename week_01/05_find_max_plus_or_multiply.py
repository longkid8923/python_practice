input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    # if len(array) == 1:
    #     ans = array[0]
    # else:
    #     idx = 1
    #     ans = array[0]
    #     while idx != len(array):
    #         plus = ans + array[idx]
    #         times = ans * array[idx]
    #         if plus > times:
    #             ans = plus
    #         else:
    #             ans = times
    #         idx += 1
    # return ans
    number = 0
    multiply_sum = 0
    for number in array:
        if number <= 1 or multiply_sum <= 1:
            multiply_sum += number
        else:
            multiply_sum *= number
    return multiply_sum


result = find_max_plus_or_multiply(input)
print(result)