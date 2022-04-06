def combine_funcs(op):
    """combine_funcs(op)(f, g)(x) = op(f(x), g(x))"""
    def combine(f, g):
        def val(x):
            return op(f(x), g(x))
        return val
    return combine

from operator import __add__
add_func = combine_funcs(__add__)
from math import sin, cos, pi
h = add_func(sin, cos)
print(h(pi / 4))