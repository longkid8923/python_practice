from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# 방문 여부를 저장할 visited 가 필요함.
# 공이 2개임 -> 4차원 배열을 활용
# visited[red_marble_row][red_marble_col][blue_marble_row][blue_marble_col]
# 3 <= x <= 10 이므로 공간적인 걱정은 할 필요 X
def move_until_wall_or_hole(r, c, diff_r, diff_c, game_map):
    move_count = 0

    while game_map[r + diff_r][c + diff_c] != '#' and game_map[r][c] != 'O':
        r += diff_r
        c += diff_c
        move_count += 1

    return r, c, move_count


def is_available_to_take_out_only_red_marble(game_map):
    n, m = len(game_map), len(game_map[0])
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    red_row, red_col, blue_row, blue_col = -1, -1, -1, -1
    queue = deque()

    for i in range(n):
        for j in range(m):
            if game_map[i][j] == 'R':
                red_row, red_col = i, j
            elif game_map[i][j] == 'B':
                blue_row, blue_col = i, j

    # 탐색을 10번까지만 가능
    queue.append((red_row, red_col, blue_row, blue_col, 1))
    visited[red_row][red_col][blue_row][blue_col] = True

    while queue:
        red_row, red_col, blue_row, blue_col, try_count = queue.popleft()
        if try_count > 10:
            break

        for i in range(4):
            next_red_row, next_red_col, red_count = move_until_wall_or_hole(red_row, red_col, dr[i], dc[i], game_map)
            next_blue_row, next_blue_col, blue_count = move_until_wall_or_hole(blue_row, blue_col, dr[i], dc[i], game_map)

            if game_map[next_blue_row][next_blue_col] == 'O':
                continue

            if game_map[next_red_row][next_red_col] == 'O':
                return True

            # 같은 위치에 서로 다른 구슬이 위치하는 것을 방지하기 위함
            # 더 많이 움직이게 될 애는 한 번 덜 움직이도록 함함
            if next_red_row == next_blue_row and next_red_col == next_blue_col:
                if red_count > blue_count:
                    next_red_row -= dr[i]
                    next_red_col -= dc[i]
                else:
                    next_blue_row -= dr[i]
                    next_blue_col -= dc[i]

            if not visited[next_red_row][next_red_col][next_blue_row][next_blue_col]:
                visited[next_red_row][next_red_col][next_blue_row][next_blue_col] = True
                queue.append((next_red_row, next_red_col, next_blue_row, next_blue_col, try_count + 1))
    # 구현해보세요!
    return False


print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다
