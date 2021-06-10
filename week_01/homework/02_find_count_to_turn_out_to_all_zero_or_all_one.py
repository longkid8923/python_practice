input = "0101010110010"


# def find_groups(string):
#     lst = list(string)
#     cnt = 1
#
#     for i in range(len(lst) - 1):
#         if lst[i] != lst[i + 1]:
#             cnt += 1
#     return cnt
#
#
# def find_count_to_turn_out_to_all_zero_or_all_one(string):
#     group_cnt = find_groups(string)
#
#     return group_cnt // 2

# 해설 코드
# input = "010101011001"
#
#
def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0

    if string[0] == '0':
        count_to_all_one += 1
    elif string[0] == '1':
        count_to_all_zero += 1

    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i + 1] == '0':
                count_to_all_one += 1
            if string[i + 1] == '1':
                count_to_all_zero += 1
    print(count_to_all_zero, count_to_all_one)
    return min(count_to_all_one, count_to_all_zero)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)


