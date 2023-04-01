# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.
import json


def read(file_in: str, file_out: str) -> None:
    new_dict = {}
    with open(file_in, 'r', encoding='utf-8') as f_in:
        for line in f_in.readlines():
            key, val = line.split()
            new_dict[key.capitalize()] = val
    with open(file_out, 'w', encoding='utf-8') as f_out:
        json.dump(new_dict, f_out,  indent=4)



def main():
    file = '/home/andrew/Documents/geekbrains/Python2023/Lections/Seminars/seminar_08/s08_task01/result.txt'
    read(file, 'result.json')


if __name__ == '__main__':
    main()
