def coincidence(lst = None, rng = None):
    appendix = []
    if lst is None or rng is None:
        return appendix
    bottom = rng[0]
    top = rng[-1]
    for item in lst:
        if isinstance(item, (int,float)) and bottom <= item <= top:
            appendix.append(item)
    return appendix

print(coincidence([None, 1, 'foo', 4, 2, 2.5, 96], range(1,4)))


