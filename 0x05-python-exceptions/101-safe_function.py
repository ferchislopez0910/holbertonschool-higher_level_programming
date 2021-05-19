#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        funct_safe = fct(*args)
        return funct_safe
    except Exception as e:
        print('Exception: {}'.format(e), file=sys.stderr)
        return None
