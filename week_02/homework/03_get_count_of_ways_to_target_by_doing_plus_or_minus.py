numbers = [1, 1, 1, 1, 1]
target_number = 3

result_cnt = 0

def get_count_of_ways_to_by_doing_plus_or_minus(array, target, current_index, current_sum):
    if current_index == len(array):
        if current_sum == target:
            global result_cnt
            result_cnt += 1
        return
    # get_all_ways_to_by_doing_plus_or_minus(array, 1, 0, +2, all_ways)
    get_count_of_ways_to_by_doing_plus_or_minus(
        array, target, current_index + 1, current_sum + array[current_index]
    )
    # get_all_ways_to_by_doing_plus_or_minus(array, 1, 0, -2, all_ways)
    get_count_of_ways_to_by_doing_plus_or_minus(
        array, target, current_index + 1, current_sum - array[current_index]
    )


get_count_of_ways_to_by_doing_plus_or_minus(numbers, target_number, 0, 0)
print(result_cnt)

