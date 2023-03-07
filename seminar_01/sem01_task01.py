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
        return "Regular year before Gregorian"
    if not a_year % EXCLUDE and not a_year % INCLUDE:
        return "Leap year"
    if not a_year % LEAP:
        return "Leap year" if a_year % 100 else "Regular year"


print(year(2000))   # Leap
print(year(1900))   # Regular
print(year(2100))   # Regular
print(year(1904))   # Leap
print(year(1584))   # Leap
print(year(1583))   # regular
print(year(1984))   # Leap
