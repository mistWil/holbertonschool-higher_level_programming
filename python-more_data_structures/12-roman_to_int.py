#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
                  "D": 500, "M": 1000}
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    result = 0
    for i in range(len(roman_string)):
        if i > 0 and rom_dict[roman_string[i]] > rom_dict[roman_string[i - 1]]:
            result += rom_dict[roman_string[i]] - 2 * rom_dict[roman_string[i - 1]]
        else:
            result += rom_dict[roman_string[i]]
    return result
