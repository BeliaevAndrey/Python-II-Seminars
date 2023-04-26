# На семинаре про декораторы был создан логирующий декоратор. Он сохранял аргументы функции и результат её работы в файл.
# Напишите аналогичный декоратор, но внутри используйте модуль logging.
from s15_logging_dec import log_deco


@log_deco
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
