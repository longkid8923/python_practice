from collections import deque  # 큐를 사용할 때 import 할 것

c = 11
b = 2

# 코니의 위치 변화
# 코니는 처음 위치에서 1초 후 1만큼, 매초마다 이전 이동거리 +1만큼 움직임
# 즉, 증가하는 속도가 1초마아 1씩 증가함

# 속도: 1 2 3 4 5 6 7 8 9 ...
# 위치: 1 3 6 10 15 ...

# 브라운의 위치 변화
# B-1, B+1, 2*B 중 하나
# 처음 위치 2
# 1-1. 2 - 1 = 1
# 1-2. 2 + 1 = 3
# 1-3. 2 * 2 = 4

# 1-1-1. 1 - 1 = 0
# 1-1-2. 1 + 1 = 2
# 1-1-3. 1 * 2 = 2

# 1-2-1. 3 - 1 = 2
# 1-2-2. 3 + 1 = 4
# 1-2-3. 3 * 2 = 6

# 모든 경우의 수를 다 나열해야 함. -> BFS 를 활용해야 할 것

# 잡았다! 라는 의미는 똑같은 시간에 똑같은 위치에 존재해야 함을 의미.
# 시간은 매 순간 + 1
# 위치는 코니도 브라운도 매 순간 바뀜

# 규칙적 -> 배열, 자유자재로 변화 -> 딕셔너리
# 각 시간마다 브라운이 갈 수 있는 위치를 저장


def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))  # 위치와 시간 정보를 모두 다 담았음. 만난다는 개념은 시간과 위치 정보가 모두 같으므로
    visited = [{} for _ in range(200001)]
    # visited[위치][시간]
    # "위치" 에 "시간"이라는 순간에 간 적이 있는가?

    while cony_loc <= 200000:
        cony_loc += time  # 코니의 위치: 현재 순간의 시간만큼 매번 위치가 변하는 규칙
        if time in visited[cony_loc]:
            return time  # 코니와 브라운이 만난 시간

        for i in range(0, len(queue)):
            current_position, current_time = queue.popleft()

            # 매 순간 시간은 1씩 증가
            new_time = current_time + 1

            # 가능한 모든 경우의 수를 큐에 다 넣어 보면서 탐색
            new_position = current_position - 1
            if 0 <= new_position <= 200000:
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if 0 <= new_position <= 200000:
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if 0 <= new_position <= 200000:
                queue.append((new_position, new_time))

        time += 1

    return -1


print(catch_me(c, b))  # 5가 나와야 합니다!