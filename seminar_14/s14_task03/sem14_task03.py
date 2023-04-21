
from string import ascii_lowercase
LETTERS = ascii_lowercase + ' '


def symbol_deleter(in_str: str) -> [str, None]:
    """
    >>> symbol_deleter("first test string") == "first test string"
    True
    >>> symbol_deleter("second test string".title()) == "second test string"
    True
    >>> symbol_deleter('Third punctuation test string [,.;:|\\/!'.capitalize()) == "third punctuation test string "
    True
    >>> symbol_deleter('Это надо удалить') == "  "
    True
    >>> symbol_deleter('This text has to be saved. А этот удален 1234098765!"№;%%::??**(()()(* ?:%:%;;!@#$%^&*(*)_+=}{[]|\\/?.,<>`~')
    'this text has to be saved     '
    """
    if not isinstance(in_str, str):
        raise TypeError("Argument is to be a string")
        # print("Argument is to be a string")
    return ''.join([letter for letter in in_str.lower() if letter in LETTERS])


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
