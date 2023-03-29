# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
import os
import shutil

BASIC_FILE_TYPES = {
    'video': ('vid1', 'vid2', 'vid3', 'vid4', ),
    'document': ('doc1', 'doc2', 'doc3', 'doc4', ),
    'text': ('txt1', 'txt2', 'txt3', 'txt4', ),
    'image': ('img1', 'img2', 'img3', 'img4', ),
}


def dir_check(dir_name: str,
              dir_path: str,
              ) -> str:
    if dir_name not in os.listdir(os.getcwd()):
        os.mkdir(dir_name)
    return os.path.join(dir_path, dir_name)


def sorter(path: str):
    os.chdir(path)
    for file in os.listdir():
        print(file)
        if os.path.isfile(file):
            cur_ext = file.rsplit('.')
            print(cur_ext)
            if len(cur_ext) == 2:
                cur_ext = cur_ext[1]
            for i_key, i_val in BASIC_FILE_TYPES.items():
                if cur_ext in i_val:
                    print(file, ': -> ', end=' ')
                    new_path = os.path.join(dir_check(dir_path=path, dir_name=i_key), file)
                    print(new_path, ': -> ', end=' ')
                    os.replace(os.path.join(path, file),
                               new_path)
                    print('worked: ', new_path)


def main():
    sorter("/home/andrew/Documents/geekbrains/Python2023/Lections/Seminars/seminar_07/s07_task07/out_dir")


if __name__ == '__main__':
    main()

