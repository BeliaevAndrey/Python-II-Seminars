# Напишите декоратор, который сохраняет в json файл параметры
# декорируемой функции и результат, который она возвращает.
# При повторном вызове файл должен расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может принимать как
# позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.
from s09t03_json_dump_params import dump_to_json_dec


@dump_to_json_dec('testfile.json')
def a_function(para1: int,
               para2: str,
               para3: str = 'a string',
               para4: int = 10) -> str:
    return str(para2) + str(para1 * para4) + str(para3)


def main():
    print(a_function(5, 'test 01'))
    print(a_function(6, 'test 02', 'another string'))
    print(a_function(7, 'test 03', para3='yet another one', para4=3))
    print(a_function(para1=8, para2='test 04',  para4=-10, para3='4'))


if __name__ == '__main__':
    main()
