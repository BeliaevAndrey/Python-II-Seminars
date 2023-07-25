# Доработаем предыдущую задачу.
# Создайте новую функцию которая генерирует файлы с разными расширениями.
# Расширения и количество файлов функция принимает в качестве параметров.
# Количество переданных расширений может быть любым.
# Количество файлов для каждого расширения различно.
# Внутри используйте вызов функции из прошлой задачи.

from random import randint as r_int
from string import ascii_lowercase as ltr
from pack_task04 import creator

MIN_FILES_AMT = 10
MAX_FILES_AMT = 42


def creator_m(extensions: [list[str], dict[str, int]]) -> None:
    if isinstance(extensions, list):
        used_amt = set()
        for ext in extensions:
            amt = r_int(MIN_FILES_AMT, MAX_FILES_AMT)
            used_amt.add(amt)
            while amt in used_amt:
                amt = r_int(MIN_FILES_AMT, MAX_FILES_AMT)
            for _ in range(amt):
                creator(ext=ext, files_amt=amt)
                used_amt.add(amt)
    elif isinstance(extensions, dict):
        for i_ext, i_amt in extensions.items():
            creator(ext=i_ext, files_amt=i_amt)


def main():
    new_exts_1 = {'ex1': 10, 'ex2': 11, 'ex3': 12, }
    creator_m(new_exts_1)
    # new_exts_2 = ['ex10', 'ex11', 'ex12', ]
    # creator_m(new_exts_2)
    # basic_file_types = {
    #     ('vid1', 'vid2', 'vid3', 'vid4',): 3,
    #     ('txt1', 'txt2', 'txt3', 'txt4',): 3,
    #     ('doc1', 'doc2', 'doc3', 'doc4',): 3,
    #     ('img1', 'img2', 'img3', 'img4',): 3,
    # }
    # for i_exts in basic_file_types.keys():
    #     creator_m({i_ext: basic_file_types[i_exts] for i_ext in i_exts})


if __name__ == '__main__':
    main()
