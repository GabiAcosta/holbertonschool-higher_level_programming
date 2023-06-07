#!/usr/bin/python3
def roman_to_int(roman_string):
    rs = roman_string
    if type(rs) != str or rs is None:
        return 0
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    converted_num = 0
    for i in range(len(rs)):
        for k, v in roman.items():
            if rs[i] == k and rs[i] in roman.keys():
                if i < len(rs) - 1 and roman.get(rs[i]) < roman.get(rs[i + 1]):
                    converted_num -= v
                else:
                    converted_num += v
    return converted_num
