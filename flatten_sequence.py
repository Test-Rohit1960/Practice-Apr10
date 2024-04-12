"""
This program flattens the given multi-dimensional sequence
"""

import src.utilities.utility_functions as uts_f

f = frozenset({3.14, 2.73})

seq = [12, 14, 88, {1: -1, 2: -2, 4: -4}, f, 3, 4, {7, 8, (9, 6, (5, 4), 2, 3)}]

print(uts_f.flatten_sequence(seq))
