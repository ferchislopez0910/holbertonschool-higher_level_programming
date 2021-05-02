#!/usr/bin/python3
for i in range(97, 123):
    if i in [101, 113]:
        continue
    print('{:c}'.format(i), end="")
