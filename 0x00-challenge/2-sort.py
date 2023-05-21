#!/usr/bin/python3
""" Sort integer arguments (ascending)
"""
import sys
import re

result = []
for arg in sys.argv[1:]:
    if not re.match(r'^-?[0-9]+$', arg):
        continue

    # convert to integer
    i_arg = int(arg)

    # insert result at the right position
    is_inserted = False
    i = 0
    size = len(result)
    while not is_inserted and i < size:
        if result[i] < i_arg:
            i += 1
        else:
            result.insert(i, i_arg)
            is_inserted = True
            break
    if not is_inserted:
        result.append(i_arg)

print(result)
