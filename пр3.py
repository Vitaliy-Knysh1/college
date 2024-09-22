lst = [1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'анаконда']

def clear_lst(lst):
    return list(set(lst))

def lst_sort(lst):
    numbers = sorted(x for x in lst if isinstance(x, int))
    strings = [x for x in lst if isinstance(x, str)]
    strings_sorted = sorted(strings)
    return numbers + strings_sorted

unique_lst = clear_lst(lst)
sorted_lst = lst_sort(unique_lst)

print(sorted_lst)
