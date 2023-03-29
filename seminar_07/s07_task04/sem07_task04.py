# Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
#   расширение
#   минимальная длина случайно сгенерированного имени, по умолчанию 6
#   максимальная длина случайно сгенерированного имени, по умолчанию 30
#   минимальное число случайных байт, записанных в файл, по умолчанию 256
#   максимальное число случайных байт, записанных в файл, по умолчанию 4096
#   количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.
from random import randint as r_int
from string import ascii_lowercase as ltr
MIN_NAME_LEN = 6
MAX_NAME_LEN = 30
MIN_BYTES_AMT = 256
MAX_BYTES_AMT = 4096
FILES_AMT = 42


def creator(ext: str,
            min_name_len: int = MIN_NAME_LEN,
            max_name_len: int = MAX_NAME_LEN,
            min_bytes_amt: int = MIN_BYTES_AMT,
            max_bytes_amt: int = MAX_BYTES_AMT,
            files_amt: int = FILES_AMT,
            ) -> None:
    def gen_name():
        return ''.join([ltr[r_int(0, len(ltr) - 1)] for _ in range(r_int(min_name_len, max_name_len))])
    for _ in range(files_amt):
        file_name = f"out_dir/{gen_name()}.{ext}"
        data = ''.join([ltr[r_int(0, len(ltr)-1)] for _ in range(r_int(min_bytes_amt, max_bytes_amt))])
        with open(file_name, 'wb') as f_out:
            f_out.write(data.encode())


def main():
    creator(ext='ext', files_amt=300)


if __name__ == '__main__':
    main()
