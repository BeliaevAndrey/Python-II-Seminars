# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Распечатайте его как pickle строку.
import pickle


def reader(file_in_path: str) -> str:
    with open(file_in_path, 'r', encoding='utf-8') as f_in:
        return f_in.read()


def to_pickle_str(line_in: str) -> None:
    print(pickle.dumps(line_in))


def main():
    file_in_path = '/home/andrew/Documents/geekbrains/Python2023/Lections/Seminars/seminar_08/s08_task06/index_04.csv'
    to_pickle_str(reader(file_in_path))


if __name__ == '__main__':
    main()
