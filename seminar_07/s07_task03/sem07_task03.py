# Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# При достижении конца более короткого файла, возвращайтесь в его начало.
import os.path

def union_func(nums: str, names: str, result: str) -> None:
    def read_line(file) -> str:
        text = file.readline()
        if text == '':
            file.seek(0)
            text = file.readline()
        return text.strip()

    with (open(nums, 'r', encoding='utf-8') as f_nums,
            open(names, 'r', encoding='utf-8') as f_names,
            open(result, 'w', encoding='utf-8') as f_out):
                len_nums = sum(1 for _ in f_nums)
                len_names = sum(1 for _ in f_names)
                for i in range(max(len_nums, len_names)):
                    l_num = read_line(f_nums)
                    l_name = read_line(f_names)
                    r_num = [*map(float, l_num.split('|'))]
                    r_num = r_num[0] * r_num[1]
                    res_line = f'{l_name} {r_num}\n'.lower() if r_num < 0 else f'{l_name} {r_num}\n'.upper()
                    f_out.write(res_line)




def main():
    union_func('file_test.txt', 'names.txt', 'result.txt')


if __name__ == '__main__':
    main()
