# Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор,
# пока он не введёт целое или вещественное число.
# Обрабатывайте не числовые данные как исключения.

def get_number(prompt: str) -> [int, float]:
    a_number = ''
    while True:
        try:
            a_number = input(prompt)
            return int(a_number)
        except ValueError:
            try:
                return float(a_number)
            except ValueError as exc:
                print(f'Only numeric values allowed. {exc.__class__.__name__}: {exc}')


def main():
    print(get_number('Input integer or float: '))


if __name__ == '__main__':
    main()
