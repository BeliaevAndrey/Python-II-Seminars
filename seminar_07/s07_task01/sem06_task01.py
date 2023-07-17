# Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции.
from random import uniform as r_flt, randint as r_int
LOWER_LIM = -1000
UPPER_LIM = 1000


def gen_num(file_name: str, str_amt: int) -> None:
    with open(file_name, 'w', encoding='utf-8') as f_out:
        for _ in range(str_amt):
            f_out.write(f'{r_int(LOWER_LIM, UPPER_LIM)}|{r_flt(LOWER_LIM, UPPER_LIM)}\n')


def main():
    gen_num(str_amt=100, file_name='file_test.txt')


if __name__ == '__main__':
    main()
