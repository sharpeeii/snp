def max_odd(array):
    maxi = None
    for item in array:
        if isinstance(item,(int,float)):
            if item % 2 != 0 and (maxi is None or item > maxi):
                maxi = item
    return maxi

