#!/usr/bin/python3
def uppercase(str):
    new_string = ""
    for i in range(len(str)):
        if (ord(str[i]) >= 97 and ord(str[i]) <= 122):
            upper_letter = chr(ord(str[i]) - 32)
            new_string += upper_letter
        else:
            new_string += str[i]
    print(new_string)
