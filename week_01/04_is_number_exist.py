input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for element in array:
        if element == number:
            return True
    return False


result = is_number_exist(7, input)
print(result)