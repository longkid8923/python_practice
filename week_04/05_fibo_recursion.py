input = 20

# 1. fibo(3) -> fibo(1)과 fibo(2)를 더하면 됨. 연산량 2번
# 2. fibo(4) -> fibo(3)과 fibo(2)를 더하면 됨. 1번 과정을 반복
# 3. fibo(2) -> 1을 반환
# 4. fibo(4) -> 연산량 3번
# ... 즉, 필요 없이 계속 했던 연산을 또 반복해야 됨. 쓸 데 없이 시간 복잡도가 커지는 효과가 나타남.


def fibo_recursion(n):
    if n <= 1:
        return n
    else:
        return fibo_recursion(n-1) + fibo_recursion(n-2)
    return


print(fibo_recursion(input))  # 6765