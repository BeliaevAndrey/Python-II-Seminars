# Дорабатываем задачу 4.
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить.
# В этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
import logging
import datetime
import argparse

MONTHS = ["янв", "фев", "мар", "апр", "мая", "июн", "июл", "авг", "сен", "окт", "ноя", "дек",]
DAYS = ["пон", "вто", "сре", "чет", "пят", "суб", "вос"]

FORMAT = ("{asctime} - {levelname} - "
          "{name} - {funcName}: {msg}")

logging.basicConfig(
    filename="date_parse.log",
    filemode='w',
    level=logging.ERROR,
    style="{",
    format=FORMAT,
)
logger = logging.getLogger(__name__)


def parse_date(date: str) -> datetime:

    try:
        week_num, day, month = date.split()
        week_num = int(week_num.split("-")[0])
    except ValueError as exc:
        logger.error(f'Parse ERROR: {exc.__class__.__name__}: {exc}')
        return None

    year = datetime.datetime.now().year
    month_num = MONTHS.index(month[:3]) + 1
    day_num = DAYS.index(day[:3])

    counter = 0
    for i in range(1, 32):
        try:
            date_in = datetime.datetime(day=i, month=month_num, year=year)
            if date_in.weekday() == day_num:
                counter += 1
                if counter == week_num:
                    return date_in
        except Exception as exc:
            print(f'\033[31m{exc.__class__.__name__}: {exc}\033[0m')
            logger.error(f'{exc.__class__.__name__}: {exc}')
            return


def arg_parser():
    # В этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
    parser = argparse.ArgumentParser(description='Find date')
    parser.add_argument('-date', metavar='date', type=str, nargs='*', help='Enter a number of weekday in month')
    parser.add_argument('-day', metavar='day', type=int, default=datetime.datetime.now().weekday(), help='Enter a number of weekday in month')
    parser.add_argument('-dow', metavar='dow', type=str, default=DAYS[datetime.datetime.now().weekday()], help='Enter a name of weekday')
    parser.add_argument('-mon', metavar='mon', type=str, default=datetime.datetime.now().month, help='Enter a month name')
    args = parser.parse_args()

    if args.date:
        return parse_date(args.date[0])
    else:
        print(date := f'{args.day}-й {args.dow} {args.mon}')
        return parse_date(date)


def main():
    print(arg_parser())


if __name__ == '__main__':
    main()
