lst = [1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'Анаконда']
lst_int = []
lst_str = []

def clean_lst(lst):
    return list(set(lst))
cleaned_lst = clean_lst(lst)

def sort_lst(lst):
    for item in lst:
        if isinstance(item, int):
            lst_int.append(item)
        elif isinstance(item, str):
            lst_str.append(item)

    lst_int.sort()
    lst_str.sort()

sort_lst(cleaned_lst)

lst = lst_int + lst_str
print(lst)
