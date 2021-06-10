input = "abcba"
input2 = "abba"


def is_palindrome(string):
    current_first = 0
    current_last = len(string)-1
    if current_first >= current_last:
        return True

    if string[current_first] == string[current_last]:
        current_first += 1
        current_last -= 1
        return is_palindrome(string[current_first:current_last+1])
    else:
        return False


print(is_palindrome(input))
print(is_palindrome(input2))
print(is_palindrome("소주만주소"))
print(is_palindrome("alias"))


# print(input2[:len(input2)//2])
# print(input2[-1:len(input2)//2-1:-1])
#
# print(input2[:len(input2)//2] == input2[-1:len(input2)//2-1:-1])