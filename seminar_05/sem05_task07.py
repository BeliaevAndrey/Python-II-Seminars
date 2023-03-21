# Создайте функцию-генератор.
# Функция генерирует N простых чисел, начиная с числа 2.
# Для проверки числа на простоту используйте правило:
# «число является простым, если делится нацело только на единицу и на себя»
from typing import Iterable


def gen_fun(lim: int) -> Iterable:
    def is_prime(num):
        if num <= 2:
            return True
        if not num % 2:
            return False
        for div in range(3, int(num ** 0.5) + 1, 2):
            if not num % div:
                return False
        return True
    for i in range(2, lim):
        if is_prime(i):
            yield i


def main():
    for i in gen_fun(int(input('Input N: '))):
        print(i)


if __name__ == '__main__':
    main()
