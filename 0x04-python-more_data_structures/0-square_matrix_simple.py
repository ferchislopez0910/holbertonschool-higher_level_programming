#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mt = []
    for i in matrix[:]:
            new_mt.append(list(map(lambda j: j ** 2, i)))
    return new_mt
