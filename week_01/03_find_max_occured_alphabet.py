input = "hello my name is sparta"


def find_alphabet_occurrence_array(string):
    if " " in string:
        string = string.replace(" ", "")
    alphabet_occurrence_array = [0] * 26

    for c in string:
        alphabet_occurrence_array[ord(c) - ord('a')] += 1

    return alphabet_occurrence_array


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = find_alphabet_occurrence_array(string)
    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence > max_occurrence:
            max_occurrence = alphabet_occurrence
            max_alphabet_index = index
    max_alphabet_index += ord('a')
    return chr(max_alphabet_index)


result = find_max_occurred_alphabet(input)
print(result)
