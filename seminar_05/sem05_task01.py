# * Пользователь вводит строку из четырёх или более целых чисел, разделённых символом “/”.
# * Сформируйте словарь, где:
#   * второе и третье число являются ключами.
#   * первое число является значением для первого ключа.
#   * четвертое и все возможные последующие числа
#   * хранятся в кортеже как значения второго ключа.

def main(in_string: str = ''):
    try:
        if not in_string:
            a, b, c, *d = map(int, input('Input string of numbers (four or more) separated by "/": ').split('/'))
            final = {b: a, c: tuple(d)}
        else:
            a, b, c, *d = map(int, in_string.split('/'))
            final = {b: a, c: tuple(d)}
    except Exception as exc:
        print('\033[31m', exc.__class__.__name__, ': ', exc, '\033[0m', sep='')
        return 'EЯR0R'
    else:
        return final


if __name__ == '__main__':
    print(main('2/ 1/ 3/ 4/ 5 '))
    print(main())
