# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

from sem06_task04 import function


def main():
    guess = {
        'first': ['one', 'two', 'three', ],
        'second': ['four', 'five', 'six', 'nine', 'fourteen', ],
        'third': ['eleven', 'twelve', 'three', 'ten', ],
        'fourth': ['eight', 'two', 'three', ],
    }
    for i_key, i_val in guess.items():
        print(f'Attempts: {function(i_key, i_val, len(i_val))}')


if __name__ == '__main__':
    main()
