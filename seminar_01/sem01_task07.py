"""
Пользователь вводит число от 1 до 999. Используя операции с числами сообщите что введено: цифра, двузначное число или трёхзначное число.
Для цифры верните её квадрат, например 5 - 25
Для двузначного числа произведение цифр, например 30 - 0
Для трёхзначного числа его зеркальное отображение, например 520 - 25
Если число не из диапазона, запросите новое число
Откажитесь от магических чисел
В коде должны быть один input и один print
"""
LIMIT = 999


def calc(num):
    if num / 10 < 1:
        return f'Digit, {num ** 2}'
    if num // 10 > 10:
        return f'Three-digits: {int(str(num)[::-1])}'
    else:
        return f'Cross-multiplied digits, {(num % 10) * (num // 10)}'


while True:
    new_num = input('Num: ')
    if new_num == 'q':
        print('Good-bye')
        raise SystemExit
    elif new_num.isdigit():
        new_num = int(new_num)
        if new_num > LIMIT:
            continue
        else:
            print(calc(new_num))
    else:
        print('Try again')
