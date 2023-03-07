"""
6.
    * Напишите программу, которая запрашивает год и проверяет его на високосность.
    * Распишите все возможные проверки в цепочке elif
    * Откажитесь от магических чисел
    * Обязательно учтите год ввода Григорианского календаря
    * В коде должны быть один input и один print
"""
LEAP = 4
EXCLUDE = 100
INCLUDE = 400
GREGORIAN = 1584


def year(a_year: int) -> str:
    if a_year < GREGORIAN:
        return "Regular"
    if ((a_year % LEAP == 0 and a_year % EXCLUDE != 0) or
            (a_year % INCLUDE == 0)):
        return "Leap"
    return "Regular"


print(year(2000))
print(year(1900))
print(year(2100))
print(year(1904))
print(year(1584))
print(year(1583))
