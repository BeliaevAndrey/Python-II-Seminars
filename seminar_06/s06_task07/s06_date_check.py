from datetime import date

_LEAP_DIVISOR = 4
_EXCLUDE = 100
_INCLUDE = 400


def _leap_year_check(a_year: int) -> bool:
    """leap year check"""
    if a_year % _EXCLUDE == 0 and a_year % _INCLUDE == 0:
        return True
    if a_year % _LEAP_DIVISOR == 0:
        return a_year % _EXCLUDE != 0


def checker(date_in: str) -> bool:
    """
    функция получает на вход дату в формате DD.MM.YYYY
    :param date_in: str
    :return: bool
    """
    if len(date_in := date_in.split('.')) != 3:
        return False
    if len(date_in[2]) > 4 or not (0 < int(date_in[2]) < 10_001):
        return False
    date_in = [*map(int, date_in)][::-1]
    if not (0 < date_in[1] <= 12):
        return False
    if 0 > date_in[2] > 31 or (date_in[1] == 2 and
                               date_in[2] == 29 and
                               not _leap_year_check(date_in[0])):
        return False
    if date_in[2] == 31 and date_in[1] not in [1, 3, 5, 7, 8, 10, 12]:
        return False
    # try:
    #     date(*date_in)
    # except ValueError:
    #     return False
    return True


if __name__ == '__main__':
    print("Not for separate use")
