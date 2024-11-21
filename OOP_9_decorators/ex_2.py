from functools import wraps


def vowel_filter(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return [el for el in result if el.lower() in 'aiuyeo']
    return wrapper


@vowel_filter
def get_letters(chars):
    """This is my func doc"""
    return chars


@vowel_filter
def concat_letters(first_list, second_list):
    return first_list + second_list


print(get_letters(['a', 'b']))
print(get_letters(['b', 'c']))
print(concat_letters(['a', 'b'], ['i', 'c']))


