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


def main1():
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


def gen_primes(amount):
    # def is_prime(num):
    #     if num <= 2:
    #         return True
    #     if not num % 2:
    #         return False
    #     for div in range(3, int(num ** 0.5) + 1, 2):
    #         if not num % div:
    #             return False
    #     return True
    def is_prime(low_lim, hi_lim, num):
        if num in (i for i in range(low_lim, hi_lim)
                   if i == 2 or (i % 2 and all(i % div for div in range(3, int(i ** 0.5) + 1, 2)))):
            return True
        return False

    k = 2
    count = 1
    while count <= amount:
        if is_prime(k - 1, k + 1, k):
            yield k
            count += 1
        k += 1


def gen_primes3(amount):
    k = 2
    count = 1
    while count <= amount:
        if k == 2 or (k % 2 and all(k % div for div in range(3, int(k ** 0.5) + 1, 2))):
            yield k
            count += 1
        k += 1


def main():
    limit = int(input('N: '))
    start = time_ns()
    result1 = [*gen_primes(limit)]
    end1 = time_ns() - start
    print(len(result1), result1)
    start = time_ns()
    result2 = [*gen_primes3(limit)]
    end2 = time_ns() - start
    print(len(result2), result2)
    print(f'{end1 = } {end2 = } {(result1 == result2) = }')


if __name__ == '__main__':
    main()
