input = "abadabac"


def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26
    for c in string:
        if not c.isalpha():
            continue
        idx = ord(c) - ord('a')
        alphabet_occurrence_array[idx] += 1

    # 내 풀이
    # ans = "_"
    # for c in string:
    #     if alphabet_occurrence_array[ord(c) - ord('a')] == 1:
    #         ans = c
    #         break
    #
    # return ans

    # 강의 풀이
    not_repeating_alphabet = []
    for i in range(len(alphabet_occurrence_array)):
        if alphabet_occurrence_array[i] == 1:
            not_repeating_alphabet.append(chr(i + ord('a')))

    for c in string:
        if c in not_repeating_alphabet:
            return c


result = find_not_repeating_character(input)
print(result)