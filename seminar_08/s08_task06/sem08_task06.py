# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестирования возьмите pickle версию файла из задачи 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
import pickle
import csv
import json


def reader(file_in_path: str) -> list[dict]:
    with open(file_in_path, 'rb') as f_in:
        out_lst = pickle.load(f_in,  encoding='utf-8')
    return out_lst


def form_lst(data_lst: list[dict]) -> list[list[str]]:
    out_lst = [[i_key for i_key in data_lst[0].keys()]]
    for dct in data_lst:
        out_lst.append([*dct.values()])
    return out_lst


def csv_write_down(data: list[list[str]], file_out_path: str) -> None:
    with open(file_out_path, 'w', encoding='utf-8') as f_out:
        csv_writer = csv.writer(f_out, dialect='excel')
        csv_writer.writerows(data)


def main():
    file_in_path = '/home/andrew/Documents/geekbrains/Python2023/Lections/Seminars/seminar_08/s08_task05/out_dir/s08_task04/index_04.bin'
    file_out_path = '/home/andrew/Documents/geekbrains/Python2023/Lections/Seminars/seminar_08/s08_task06/index_04.csv'
    csv_write_down(form_lst(reader(file_in_path)), file_out_path)


if __name__ == '__main__':
    main()
