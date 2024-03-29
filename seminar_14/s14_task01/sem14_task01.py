# Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

from string import ascii_lowercase
LETTERS = ascii_lowercase + ' '


def symbol_deleter(in_str: str) -> str:
    if not isinstance(in_str, str):
        raise TypeError("Argument is to be a string")
    return ''.join([letter for letter in in_str.lower() if letter in LETTERS])


def main():
    print(symbol_deleter('This text is to be saved. А этот текст должен быть удален 1234098765'
                         '!"№;%%::?? ** (() ()( *  ?: %: %;;!@#$%^&*(*)_+=}{[]|\\/?.,<>`~'))


if __name__ == '__main__':
    main()
