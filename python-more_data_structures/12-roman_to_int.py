#!/usr/bin/python3
def roman_to_int(roman_string):
    dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
            "D": 500, "M": 1000}
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    result = 0
    for i in range(len(roman_string)):
        current = roman_string[i]
        previous = roman_string[i - 1]
        if i > 0 and dict[current] > dict[previous]:
            result += dict[current] - 2 * dict[previous]
        else:
            result += dict[current]
    return result
