# Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.

# date_format = '1-й четверг ноября'
from datetime import date, datetime as dt
import logging

MONTH_TRANSLATE = {
    'янв': 'January', 'фев': 'February', 'мар': 'March', 'апр': 'April',
    'мая': 'May', 'июн': 'June', 'июл': 'July', 'авг': 'August',
    'сен': 'September', 'окт': 'October', 'ноя': 'November', 'дек': 'December'
}
WEEKDAYS_TRANSLATE = {'пон': 'Monday', 'вто': 'Tuesday', 'сре': 'Wednesday',
                      'чет': 'Thursday', 'пят': 'Friday', 'суб': 'Saturday', 'вос': 'Sunday'}

logging.basicConfig(
    filename="data.log",
    level=logging.INFO,
    style="{",
)
logger = logging.getLogger(__name__)


def parse_date(date_in: str):
    try:
        year = date.today().year
        week_of_month = int(date_in.split('-')[0])
        day_name, month = date_in.split()[1:]
        day_name_eng = WEEKDAYS_TRANSLATE[day_name[:3]]
        searched = dt.strptime(f'{MONTH_TRANSLATE[month[:3]]} {year}', "%B %Y")
        new_day = (searched.day + (week_of_month - 1) * 7)
        week_day = searched.strftime("%A")
        while week_day != day_name_eng:
            new_day += 1
            searched = searched.replace(day=new_day)
            week_day = searched.strftime("%A")
        return date_in, searched
    except Exception as exc:
        logger.info(f'{date_in} : {exc.__class__.__name__}: {exc}')
        return date_in, f'{exc.__class__.__name__}: {exc}'


def check_date(date_in: str):
    print('CHECKER:',
          dt.strptime(date_in, "%Y-%m-%d").
          strftime("%Y-%m-%d; day-of-year: %j; weekday: %w; day-name: %A; week-of-year %W;"))


def main():
    print("{:30} -> {}".format(*parse_date('1-й четверг ноября')))    # 2023-11-02 check_date('2023-11-02')
    print("{:30} -> {}".format(*parse_date('3-я среда мая')))         # 2023-05-17 check_date('2023-05-17')
    print("{:30} -> {}".format(*parse_date('14-я среда апреля')))      # ERROR
    print("{:30} -> {}".format(*parse_date('3-я суббота февраля')))   # 2023-02-18 check_date('2023-02-18')
    print("{:30} -> {}".format(*parse_date('4-й вторник апреля')))    # 2023-04-25 check_date('2023-04-25')
    print("{:30} -> {}".format(*parse_date('4-я среда апреля')))      # 2023-04-26 check_date('2023-04-26')


if __name__ == '__main__':
    main()
