#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        i = 0
        print_count = 0
        while i < x:
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                print_count += 1
            i += 1
        print()
        return print_count
    except (ValueError, TypeError):
        print()
        return print_count
