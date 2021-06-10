top_heights = [6, 9, 5, 7, 4]


# 1차: 6  9  5  7  4
#     4를 먼저 빼고 7, 5, 9, 6 순으로 따져보고 제일 먼저 만나는 7의 인덱스를 ans 배열에 집어넣음
# 2차: 6  9  5  7
#     다음으로 7도 빼고 따져 보고 다음으로 만나는 9의 인덱스를 ans 배열에 집어넣음
# 3차: 6  9  5
# 4차: 6  9
# ...
# 하나씩을 계속 빼고 생각한다. 배열이 빌 때까지 계속 뺀다.
# 늦게 들어간 것부터 먼저 빼게 되므로 스택으로 생각해 볼것.

def get_receiver_top_orders(heights):
    ans = [0] * len(heights)
    while heights:
        height = heights.pop()
        for idx in range(len(heights) - 1, 0, -1):
            if heights[idx] > height:
                ans[len(heights)] = idx + 1
                break

    return ans


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

arr = [1, 2, 3, 4, 5]
arr[3] = 3
print(arr)
