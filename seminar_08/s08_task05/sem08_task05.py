# Напишите функцию, которая ищет json файлы в указанной директории
# и сохраняет их содержимое в виде одноимённых pickle файлов.
import pickle
import json
import os


def searcher(path: str) -> list[list[str]]:
    files_lst = []
    if not os.path.isdir(path):
        raise IOError("Obtained path is noa a directory")
    for path_str in os.walk(path):
        for file_nm in path_str[-1]:
            if file_nm.endswith('.json'):
                files_lst.append([os.path.abspath(path_str[0]), file_nm])
    return files_lst


def build_tree(files_lst: list, out_path: str = '.') -> str:
    if not os.path.isdir(out_path):
        os.mkdir(out_path)
    os.chdir(out_path)
    for line in files_lst:
        if not os.path.isdir(os.path.split(line[0])[-1]):
            os.mkdir(os.path.split(line[0])[-1])
    return os.getcwd()


def serialize_to_disk(file_lst: list) -> None:
    json_dicts = {}
    for file_rec in file_lst:
        file_path = os.path.join(*file_rec)
        file_dir = os.path.split(file_rec[0])[-1]
        file_name = file_rec[-1]
        with open(file_path, 'r', encoding='utf-8') as f_in:
            json_dicts[(file_dir, file_name.replace('.json', '.bin'))] = json.load(f_in)
    for nm, dct in json_dicts.items():
        with open(os.path.join(os.getcwd(), *nm), 'wb') as f_out:
            pickle.dump(dct, f_out)


def main():
    path_in = '../'
    path_out = './s08_task05/out_dir'
    files_lst = searcher(path_in)
    build_tree(files_lst, path_out)
    serialize_to_disk(files_lst)


if __name__ == '__main__':
    main()
