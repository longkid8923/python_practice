array_a = [1, 2, 3, 5, 9]
array_b = [2, 4, 6, 7, 8, 10]


def merge(array1, array2):
    array_c = []
    current_1, current_2 = 0, 0

    while current_1 != len(array1) and current_2 != len(array2):
        if array1[current_1] > array2[current_2]:
            array_c.append(array2[current_2])
            current_2 += 1
        else:
            array_c.append(array1[current_1])
            current_1 += 1

    if current_1 == len(array1):
        for i in range(current_2, len(array2)):
            array_c.append(array2[current_2])
            current_2 += 1
    else:
        for i in range(current_1, len(array1)):
            array_c.append(array1[current_1])
            current_1 += 1

    return array_c


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!