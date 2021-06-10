shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["사이다", "오뎅", "콜라", "만두", "떡볶이"]


def is_in(target, lst):
    lst = sorted(lst)
    current_min = 0
    current_max = len(lst) - 1
    current_guess = (current_min + current_max) // 2

    while current_min <= current_max:
        if lst[current_guess] == target:
            return True
        elif lst[current_guess] > target:
            current_max = current_guess - 1
        else:
            current_min = current_guess + 1
        current_guess = (current_min + current_max) // 2

    return False


def is_available_to_order(menus, orders):
    true_lst = []
    for o in orders:
        if is_in(o, menus):
            true_lst.append(o)
    if len(true_lst) == len(orders):
        return True

    return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)


