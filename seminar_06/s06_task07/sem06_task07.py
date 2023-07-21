# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# * Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# * Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# * Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# * Проверку года на високосность вынести в отдельную защищённую функцию.
from s06_date_check import *


def main():
    print(date_c := "29.02.1564", checker(date_c))
    print(date_c := "29.02.2000", checker(date_c))
    print(date_c := "29.02.1960", checker(date_c))
    print(date_c := "31.12.9999", checker(date_c))
    print(date_c := f"31.12.{(9999 + 1):_d}", checker(date_c))
    print(date_c := "31.12.1", checker(date_c))
    print(date_c := "31.12.-1", checker(date_c))
    print(date_c := "12.04.1961", checker(date_c))
    print(date_c := "12/04/1961", checker(date_c))
    print(date_c := "12.04.1961", checker(date_c))
    print(date_c := "32.04.1961", checker(date_c))
    print(date_c := "12.34.1961", checker(date_c))
    print(date_c := "31.04.1961", checker(date_c))
    print(date_c := "30.04.1961", checker(date_c))


if __name__ == '__main__':
    main()
