input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    max_num = -1
    for n in array:
        if n > max_num:
            max_num = n
    return max_num


result = find_max_num(input)
print(result)