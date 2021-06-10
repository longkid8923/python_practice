seat_count = 9
vip_seat_array = [4, 7]


# 1. i 번째 좌석에 i 번 티켓을 가진 사람이 그대로 앉는 경우 -> 0 ~ (i - 1)번째 좌석까지는 마음대로 배치
# 2. i 번재 티켓을 가진 사람이 i - 1 번째 자리에 앉는 경우 -> 0 ~ (i - 2)번째 좌석까지는 마음대로 배치
# 결국 이웃한 자리 밖에 못 옮기기 때문에 1과 2번의 경우의 수를 합하는 것이 전체 경우의 수가 된다.
# F(N) = F(N - 1) + F(N - 2)
memo = {
    1: 1,
    2: 2
}


def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n-1, fibo_memo) + fibo_dynamic_programming(n-2, fibo_memo)
    fibo_memo[n] = nth_fibo

    return nth_fibo


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    all_ways = 1
    current_index = 0

    for fixed_seat in fixed_seat_array:
        fixed_seat_index = fixed_seat - 1
        count_of_ways = fibo_dynamic_programming(fixed_seat_index - current_index, memo)
        all_ways *= count_of_ways
        current_index = fixed_seat_index + 1

    count_of_ways = fibo_dynamic_programming(total_count - current_index, memo)
    all_ways *= count_of_ways

    return all_ways


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))

lst = list([[1, 2, 3]])
print(lst)