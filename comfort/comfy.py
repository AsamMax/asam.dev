def firstTrue(*arg):
    for el in arg:
        if el:
            return el
    return None