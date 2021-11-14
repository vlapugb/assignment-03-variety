def sum_some(numbers, indices):
    """
    Вернуть сумму элементов из numbers, на позициях, записанных в indices
    sum_some([1, 2, 3], [0, 1, 1]) -> 5 = (1+2+2)
    """
    return sum([numbers[i] for i in indices])


def replace_range(a, b, x, y):
    """
    Заменить подмассив массива a с индексами от x до y на массив b
    replace_range([1, 2, 3, 4], [7, 8, 9], 0, 1) -> [7, 8, 9, 3, 4]
    """
    return a[:x]+b+a[y+1:]


def sum_list(a):
    """
    Рекурсивно просуммировать элементы массива a
    sum_list([1, 2, 3]) -> 6
    """
    def temp_func(a):
        t=a[:-1]
        t[-1]+=a[-1]
        return t
    if len(a)==0:
        return 0
    if len(a)==1:
        return a[0]
    else:
        return sum_list(temp_func(a))


def signs(a):
    """
    Расставьте между элементами массива a знаки отношений "меньше", "равно" или "больше"
    signs([2, 8, 4, 4]) -> [2, '<', 8, '>', 4, '=', 4]
    """
    temp_array = []
    for i, el in enumerate(a[:-1]):
        temp_array += [el]
        if a[i + 1] > el:
            temp_array += ["<"]
        elif a[i + 1] < el:
            temp_array += [">"]
        else:
            temp_array += ["="]
    temp_array += [a[-1]]
    return temp_array
