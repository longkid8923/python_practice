current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 북: row -1, col 0, 동: row 0, col +1, 남: row +1, col 0, 서: row 0, col -1
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# 북 0 동 1 남 2 서 3(index 로)
# 북쪽에서 왼쪽으로 회전하면: 서쪽, 0 -> 3번 인덱스
# 동쪽에서 왼쪽으로 회전: 북쪽, 1 -> 0
# 남쪽에서 왼쪽으로 회전: 동쪽, 2 -> 1
# 서쪽에서 왼쪽으로 회전: 남쪽, 3 -> 2

# 북쪽에서 후진하면(왼쪽으로 두 번 회전): 남쪽, 0 -> 2
# 동 후진: 서, 1 -> 3
# 남 후진: 북, 2 -> 0
# 서 후진: 동, 3 -> 1

# 회전 함수 구현
def get_d_index_when_rotate_to_left(d):
    return (d + 3) % 4


# 후진 함수 구현
def get_d_index_when_go_back(d):
    return (d + 2) % 4


# 1. 현재 위치를 청소한다.
# bfs를 구현 visited = [1, 2, 3]
# 0은 청소하지 않은 장소
# 1은 청소하지 못하는 장소
# 2는 청소한 장소

# 2. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로
# 탐색 진행
# -> 방향

# a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면
# 그 방향으로 회전한 다음 한 칸으 전진하고 1번부터 진행

# b. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고
# 2번으로 돌아감.
# -> 현재 본 방향에서 청소할 공간이 없으면 다시 왼쪽으로 회전

# c. 네 방향 모두 청소가 되어 있거나 벽인 경우
# 바라보는 방향을 유지한 채로 한 칸 후진 하고 2번으로 돌아감.
# -> 모든 방향이 청소되어 있다면, 뒤로 한 칸 후진

# d. 네 방향 모두 청소가 이미 되어 있거나 벽이면서,
# 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.


def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    n = len(room_map)
    m = len(room_map[0])
    count_of_departments_cleaned = 1
    room_map[r][c] = 2
    queue = list([[r, c, d]])

    while queue:
        r, c, d = queue.pop(0)
        temp_d = d

        for i in range(4):
            temp_d = get_d_index_when_rotate_to_left(temp_d)
            new_r, new_c = r + dr[temp_d], c + dc[temp_d]

            if 0 <= new_r < n and 0 <= new_c < m and current_room_map[new_r][new_c] == 0:
                count_of_departments_cleaned += 1
                room_map[new_r][new_c] = 2
                queue.append([new_r, new_c, temp_d])
                break
            # c. 네 방향 모두 청소가 되어 있거나 벽인 경우
            # 바라보는 방향을 유지한 채로 한 칸 후진하고 2번으로 돌아감
            elif i == 3:  # 마지막 인덱스까지 왔는데(네 방향 모두 확인 했는데도 못 찾았을 때)
                new_r, new_c = r + dr[get_d_index_when_go_back(temp_d)], c + dc[get_d_index_when_go_back(temp_d)]
                queue.append([new_r, new_c, temp_d])

                # d. 네 방향 모두 청소가 이미 되어 있거나 벽이면서,
                # 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
                if current_room_map[new_r][new_c] == 1:
                    return count_of_departments_cleaned



# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
