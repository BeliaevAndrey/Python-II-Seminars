# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.
import json


def read_csv(csv_file: str) -> list[list[str]]:
    result = []
    with open(csv_file, 'r', encoding='utf-8') as f_in:
        for line in f_in.readlines():
            result.append(line.strip().split(';'))
    return result


def to_format(data: list[list[str]]) -> list[dict[str]]:
    data_lst = []
    for record in data:
        user_hash = hash(int(record[1])) + hash(record[2])
        data_lst.append(dict(user_hash=user_hash,
                             user_id=f'{record[1]:0>10}',
                             user_name=record[2].capitalize(),
                             access_level=record[0]))
    return data_lst


def write_json(data: list[dict[str, str]],
               json_file: str) -> None:
    with open(json_file, 'w', encoding='utf-8') as f_out:
        json.dump(data, f_out, indent=4)


def starter(file_in: str, file_out: str) -> None:
    write_json(to_format(read_csv(file_in)), file_out)


def main():
    file_in_name = 'index.csv'
    file_out_name = 'index_04.json'
    starter(file_in=file_in_name, file_out=file_out_name)


if __name__ == '__main__':
    main()
