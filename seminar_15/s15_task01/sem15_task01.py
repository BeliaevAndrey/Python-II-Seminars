# Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.
from __future__ import annotations

import logging

logger = logging.getLogger(__name__)
FORMAT = '{asctime:20} - {levelname:10} - In "{name}" : {msg}'
logging.basicConfig(format=FORMAT, style="{",
                    filename='sem15_task01.log',
                    filemode='w', level=logging.ERROR)


def divider(left: [int, float], right: [int, float]) -> float | None:
    try:
        return left / right
    except ZeroDivisionError as exc:
        logger.error(msg=f'{exc}')
        return


def main():
    print(divider(10, 2))
    print(divider(10, 0))


if __name__ == '__main__':
    main()
