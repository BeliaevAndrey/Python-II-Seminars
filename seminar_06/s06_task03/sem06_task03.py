# * Улучшаем задачу 2.
# * Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# * Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# * Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.
from random import randint as r_int
from sys import argv


def guess(lo: int, hi: int = 100, attempts_amt: int = 3) -> bool:
    lo, hi = sorted((hi, lo))
    number = r_int(lo, hi)
    count: int = 0
    while count < attempts_amt:
        count += 1
        print(f'attempt: {count}')
        guess_num = int(input('Enter integer: '))
        if guess_num == number:
            return True
        elif guess_num < number:
            print("Your number is lesser")
        else:
            print("Your number is greater")
    print(f'the number was: {number}')
    return False


if __name__ == '__main__':
    params = 10,
    if not argv:
        low = 10
        high = 100
        attempts = 10
    else:
        params = map(int, argv[1:])
        print('limits:', *params)

    if guess(*params):
        print('Right')
    else:
        print('Wrong')
