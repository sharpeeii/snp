chaotic_array = [12,1,1,12, 1, 5, 885, 12, 31, 998]


def sort_list(lst: list):
    if not lst:
        return lst
    minimal = min(lst)
    maximal = max(lst)
    for i in range(len(lst)):
        if lst[i] == minimal:
            lst[i] = maximal
        elif lst[i] == maximal:
            lst[i] = minimal
    lst.append(minimal)
    return lst 

print(sort_list([]))
print(sort_list([2,4,6,8]))
print(sort_list([1]))
print(sort_list([1,2,1,3]))
print(sort_list(chaotic_array))
