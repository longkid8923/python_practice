input = 100

# dynamic programming 조건
# 1. 반복되는 부분 문제(overlapping sub problems)
# 2. memoization 필요


# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}

# 1. 만약 메모에 있으면 그 값 바로 반환
# 2. 없으면 아까의 수식처럼
# 3  그 값을 다시 메모에 기록한다.


def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n-1, fibo_memo) + fibo_dynamic_programming(n-2, fibo_memo)
    fibo_memo[n] = nth_fibo

    return nth_fibo


print(fibo_dynamic_programming(input, memo))