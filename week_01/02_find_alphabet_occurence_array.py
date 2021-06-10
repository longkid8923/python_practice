def find_alphabet_occurrence_array(string):
    if " " in string:
        string = string.replace(" ", "")
    alphabet_occurrence_array = [0] * 26

    for c in string:
        alphabet_occurrence_array[ord(c) - ord('a')] += 1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))
print(int('a'))