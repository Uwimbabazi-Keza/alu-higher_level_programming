#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    if roman_string and type(roman_string) == str:
        n = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in range(len(roman_string)):
            if i != (len(roman_string) - 1) and \
                    n[roman_string[i]] < n[roman_string[i + 1]]:
                result += int(n[roman_string[i + 1]] -
                              (n[roman_string[i + 1]] / 10))
                result -= n[roman_string[i + 1]]
            else:
                result += n[roman_string[i]]
    return result
