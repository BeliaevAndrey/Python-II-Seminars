# Дорабатываем функции из предыдущих задач.
# Генерируйте файлы в указанную директорию — отдельный параметр функции.
# Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
import os
from pack_task05 import creator_m

DEFAULT_DIR_PATH = os.getcwd()


def dir_check(dir_name: str,
              dir_path: str = DEFAULT_DIR_PATH,
              ) -> str:
    os.chdir(dir_path)
    if dir_name not in os.listdir(os.getcwd()):
        os.mkdir(dir_name)
    return os.path.join(dir_path, dir_name)


def creator_m2(extensions: [list[str], dict[str, int]],
               dir_name: str,
               dir_path: str = DEFAULT_DIR_PATH):
    os.chdir(dir_check(dir_name, dir_path))
    creator_m(extensions)


def main():
    new_exts_1 = {'ex1': 10, 'ex2': 11, 'ex3': 12, }
    creator_m2(new_exts_1, 'tst_directory')


if __name__ == '__main__':
    main()
