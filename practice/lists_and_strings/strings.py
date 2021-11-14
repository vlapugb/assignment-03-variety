def reverse(s):
    """
    Вернуть исходную строку, записанную наоборот
    reverse('abc') -> 'cba'
    """
    return s[::-1]


def swap_case(s):
    """
    Заменить регистр каждого символа, входящего в строку, на противоположный
    swap_case('Hello world') -> 'hELLO WORLD'
    """
    return "".join([i.upper() if i.islower() else i.lower() for i in s])

def censor_words(s, blacklist):
    """
    Вернуть исходную строку, в которой слова из blacklist заменены на звездочки
    censor_words('hello world', ['hello']) -> '***** world')
    """
    return ' '.join(["*" * len(a) if a in blacklist else a for a in s.split(' ')])


def remove_duplicates(s):
    """
    Удалить идущие подряд повторы слов в строке
    remove_duplicates('hello nice nice world hello') -> 'hello nice world hello'
    """
    temp_w = []
    temp_str = ""
    for i in s.split(" "):
        if i != temp_str:
            temp_w.append(i)
        temp_str = i
    return ' '.join(temp_w)


def parentheses(s):
    """
    Проверить, закрыты ли все пары круглых скобок в строке
    parentheses( '(abc(1+2))' )    -> True
    parentheses( '(lalala' )       -> False - скобка не закрыта
    parentheses( '(hello)world)' ) -> False - слишком много закрывающих скобок
    """
    def prove_function(a):
        opened = a.count(")")
        closed = a.count("(")
        if closed > opened:
            return False
        return True

    if s.count(")") == s.count("("):
        for i in range(len(s)):
            if not prove_function(s[:i]):
                return False
        return True
    return False
