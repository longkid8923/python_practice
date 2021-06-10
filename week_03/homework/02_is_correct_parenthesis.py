s = "(())()"


# 1. 괄호 열림
# 2. 괄호 또 열림 "(("
# 3. 괄호 닫힘. 아까 열린 것 중 가장 현재 열린 괄호는...
# 4. 괄호 닫힘. 아까 열린 것 중 가장 현재 열린 괄호는...
# ...

# 바로 직전에 조회한 괄호를 저장해야 한다. -> stack 자료구조

def is_correct_parenthesis(string):
    stack = []

    for i in range(len(string)):
        if string[i] == '(':
            stack.append(string[i])
        elif string[i] == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!
