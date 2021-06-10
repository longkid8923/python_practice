from collections import deque

balanced_parentheses_string = "()))((()"


# 균형잡힌 괄호 문자열 -> 올바른 괄호 문자열
# 올바른 괄호 문자열?

def is_correct_parentheses(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack:
            stack.pop()

    return len(stack) == 0


def separate_to_uv(string):
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""
    while queue:
        char = queue.popleft()
        u += char
        if char == '(':
            left += 1
        else:
            right += 1

        if left == right:  # u 는 더 이상 쪼갤 수 없는 균형 잡힌 문자열이어야 함.
            break

    v = ''.join(list(queue))

    return u, v


def reverse_parenthesis(string):
    reversed_string = ""
    for ch in string:
        if ch == '(':
            reversed_string += ')'
        else:
            reversed_string += '('

    return reversed_string


def change_to_correct_parenthesis(string):
    if string == "":
        return ""
    # 2. 문자열 w를 두 균형잡힌 괄호 문자열" u, v로 분리
    # u는 균형잡힌 괄호 문자열로 더 이상 분리할 수 없어야 함.
    # v는 빈 문자열이 될 수도 있음
    # ( 와 ) 의 개수가 같아야 함.
    u, v = separate_to_uv(string)

    # 3. 문자열 u 가 올바른 괄호 문자열 이라면 문자열 v에 대해 1단계부터 다시 수행
    if is_correct_parentheses(u):
        return u + change_to_correct_parenthesis(v)

    # 4. 문자열 u 가 올바른 괄호 문자열이 아니라면 아래 과정 수행
    # 4-1. 빈 문자열에 첫 번째 문자로 ( 를 붙임
    # 4-2. 문자열 v 에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙임
    # 4-3. )를 다시 붙임
    # 4-4. u 의 첫 번째 문자와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어 뒤에 붙임.
    else:
        return '(' + change_to_correct_parenthesis(v) + ')' + reverse_parenthesis(u[1:-1])


def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parentheses(balanced_parentheses_string):
        return balanced_parentheses_string
    else:
        return change_to_correct_parenthesis(balanced_parentheses_string)


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!
# print(separate_to_uv(balanced_parentheses_string))