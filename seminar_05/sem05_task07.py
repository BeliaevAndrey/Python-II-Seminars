# Создайте функцию-генератор.
# Функция генерирует N простых чисел, начиная с числа 2.
# Для проверки числа на простоту используйте правило:
# «число является простым, если делится нацело только на единицу и на себя»
from typing import Iterable
from time import time_ns


def gen_fun2(lim: int) -> Iterable:
    yield from (i for i in range(2, lim)
                if i == 2 or (i % 2 and
                all(i % div for div in range(3, int(i ** 0.5) + 1, 2))))


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
    result1 = []
    result2 = []
    lim = int(input('Input N: '))
    start = time_ns()
    for i in gen_fun(lim):
        result1.append(i)
    end1 = time_ns() - start
    start = time_ns()
    for i in gen_fun2(lim):
        result2.append(i)
    end2 = time_ns() - start
    print(result1)
    print(result2)
    print(f'Wasted: {end1} {end2}')
    assert (result1 == result2)


if __name__ == '__main__':
    main()
