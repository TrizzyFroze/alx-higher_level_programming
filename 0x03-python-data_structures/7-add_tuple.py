#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a, len_b = len(tuple_a), len(tuple_b)
    new_tuple = ((tuple_a[0] if len_a >= 1 else 0) +
