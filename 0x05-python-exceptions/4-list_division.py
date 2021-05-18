#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            val_end = my_list_1[i]/my_list_2[i]
        except TypeError:
            val_end = 0
            print('wrong type')
        except ZeroDivisionError:
            val_end = 0
            print('division by 0')
        except IndexError:
            val_end = 0
            print('out of range')
        finally:
            result.append(val_end)
    return result
