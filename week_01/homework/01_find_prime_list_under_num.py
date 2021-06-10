input = 20


def is_prime(number):
    if number == 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def find_prime_list_under_number(number):
    prime_list = []
    for i in range(1, number + 1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list


result = find_prime_list_under_number(input)
print(result)
