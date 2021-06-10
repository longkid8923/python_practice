import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


# 1. 현재 재고의 상태에 따라 최곳값을 받아야 함 -> 동적으로 변경되는 상황(재고 상황)
# 2. 제일 많은 값, 제일 큰 값을 뽑아내야 함.
# 3. 데이터를 넣을 때마다 최댓값을 동적으로 변경시키며
# 4. 최솟/최댓값을 바로 꺼낼 수 있는 구조를 사용하면 좋음.

def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    ans = 0
    last_added_date_index = 0  # 현재 재고량을 통해서 봤을 때 버틸 수 있는 날짜인지를 판단하기 위한 인덱스
    max_heap = []

    while stock <= k:
        while last_added_date_index < len(dates) and dates[last_added_date_index] <= stock:
            heapq.heappush(max_heap, supplies[last_added_date_index] * (-1))
            last_added_date_index += 1
            print(max_heap)

        ans += 1
        heappop = heapq.heappop(max_heap)
        stock += heappop * (-1)
    return ans


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
