# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и значение по умолчанию.
# При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.

from typing import Any, Hashable


def dct_getter(in_dct: dict, key: Hashable, default_value: Any) -> Any:
    try:
        return in_dct[key]
    except KeyError:
        return default_value


def main():
    tst_dct = {'abc': 123, 123: 'abc', (1, 2, 3): 'a, b, c'}
    print(dct_getter(tst_dct, 123, -1))
    print(dct_getter(tst_dct, 'abc', -3))
    print(dct_getter(tst_dct, (1, 2, 3), -2))
    print(dct_getter(tst_dct, (1, 3), -2))
    print(dct_getter(tst_dct, 'a', -2))


if __name__ == '__main__':
    main()
