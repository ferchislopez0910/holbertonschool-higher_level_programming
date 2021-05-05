def replace_in_list(my_list, idx, element):
    ln = len(my_list)
    if idx < 0:
        return my_list
    elif idx > ln:
        return my_list
    else:
        for i in range(ln):
            if i == idx:
                my_list[idx] = element
                return (my_list)
