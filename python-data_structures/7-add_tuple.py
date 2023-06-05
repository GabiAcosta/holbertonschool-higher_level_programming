#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    new_t1 = tuple_a + (0, 0)
    new_t2 = tuple_b + (0, 0)
    new_tuple = (new_t1[0] + new_t2[0]), (new_t1[1] + new_t2[1])
    return new_tuple
