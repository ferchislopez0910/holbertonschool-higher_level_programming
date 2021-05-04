#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    result = add(a, b)
    resultsub = sub(a, b)
    resultmul = mul(a, b)
    resultdiv = div(a, b)
    print('{} + {} = {}'.format(a, b, result))
    print('{} + {} = {}'.format(a, b, resultsub))
    print('{} + {} = {}'.format(a, b, resultmul))
    print('{} + {} = {}'.format(a, b, resultdiv))
