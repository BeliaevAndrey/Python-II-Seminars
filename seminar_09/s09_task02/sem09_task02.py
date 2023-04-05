# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов.
from typing import Callable
from random import randint


def decorator(func: Callable) -> Callable:
    range_lim = [*range(1, 101)]
    attempts_amt_lim = [*range(1, 11)]

    def wrapper(num_sc, attempts):
        if num_sc not in range_lim:
            num_sc = randint(1, 100)
        if attempts not in attempts_amt_lim:
            attempts = randint(1, 10)
        func(num_sc, attempts)

    return wrapper


@decorator
def guess(num_sc, attempts) -> None:

    while attempts:
        print(f'left {attempts} attempts.', end=' ')
        attempts -= 1
        num = int(input('Input a number: '))
        if num == num_sc:
            print(f'Number found: {num}')
            break
        else:
            advice = ['lesser', 'greater']
            print(f'Your number is {advice[num > num_sc]} then right')
    else:
        print(f'You loose. Right number is {num_sc}')


def main():
    guess(345353, -2342342)


if __name__ == '__main__':
    main()
