# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# Полученные имена сохраните в файл.

from random import randint as r_int
from string import ascii_lowercase as letters

NAME_LEN_U_LIM = 8
NAME_LEN_L_LIM = 4

VOWELS = set('aeiouy')


def name_gen(count: int,
             file_name: str = 'names.txt') -> None:
    def gen():
        return ''.join([letters[r_int(0, len(letters) - 1)]
                        for _ in range(r_int(NAME_LEN_L_LIM, NAME_LEN_U_LIM))]).capitalize()

    for _ in range(count):
        name = gen()
        while not set(name).intersection(VOWELS):
            name = gen()

        with open(file_name, 'a', encoding='utf-8') as f_out:
            f_out.write(name + '\n')


def main():
    name_gen(count=100)


if __name__ == '__main__':
    main()
