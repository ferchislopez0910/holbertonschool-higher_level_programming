#!/usr/bin/python3
for i in reversed(range(97, 123)):
    if i % 2 == 1:
        i -= 32
        print('{:c}'.format(i), end="")
    else:
        print('{:c}'.format(i), end="")
