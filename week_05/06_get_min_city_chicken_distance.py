import itertools, sys

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]


# 여러개 중에서 M개를 고를 뒤, 모든 치킨거리의 합이 가장 작게 되는 경우를 찾음.
# -> 여러 개 중에서 특정 개수를 뽑는 경우의 스
# -> 모든 경우의 수를 다 구해야 함(조합)

def get_min_city_chicken_distance(n, m, city_map):
    chicken_location_list = []
    home_location_list = []
    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1:
                home_location_list.append([i, j])
            elif city_map[i][j] == 2:
                chicken_location_list.append([i, j])

    # 치킨집들 중 m개를 골라내는 조합을 리스트로 나타내 줌
    chicken_location_m_combinations = list(itertools.combinations(chicken_location_list, m))
    min_distance_of_m_combinations = sys.maxsize

    print(chicken_location_m_combinations)
    for chicken_location_m_combination in chicken_location_m_combinations:
        city_chicken_distance = 0  # 도시의 치킨 거리를 변수로 받고 초기화
        for home_r, home_c in home_location_list:
            min_home_chicken_distance = sys.maxsize  # 각 집의 위치에 대한 치킨거리 변수 초기화
            # 치킨 거리는 집에서 가장 가까운 치킨집과의 거리로 정의됨
            for chicken_location in chicken_location_m_combination:
                min_home_chicken_distance = min(
                    min_home_chicken_distance,
                    abs(home_r - chicken_location[0]) + abs(home_c - chicken_location[1])
                )

            city_chicken_distance += min_home_chicken_distance  # 도시의 치킨 거리는 각 집의 치킨거리의 합

        # 각 조합에 대한 반복문 한 번 돌 때마다 비교해보고 최소값을 갖고 와라.
        min_distance_of_m_combinations = min(min_distance_of_m_combinations, city_chicken_distance)

    return min_distance_of_m_combinations


# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!

