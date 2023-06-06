#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return
    max_value = 0
    for k, v in a_dictionary.items():
        if max_value < v:
            max_value = v
    for k, v in a_dictionary.items():
        if max_value == v:
            return k
