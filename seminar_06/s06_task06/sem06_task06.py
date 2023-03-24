# Добавьте в модуль с загадками функцию, которая принимает на вход строку
# (текст загадки) и число (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из
# защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.

import sem06_task04 as prev


def main():
    guess = {
        'first': ['one', 'two', 'three', ],
        'second': ['four', 'five', 'six', 'nine', 'fourteen', ],
        'third': ['eleven', 'twelve', 'three', 'ten', ],
        'fourth': ['eight', 'two', 'three', ],
    }
    for i_key, i_val in guess.items():
        prev.function(i_key, i_val, len(i_val))
        # print(f'Attempts: {prev.guess_number_fun(i_key, i_val, len(i_val))}')

    print(f'\n===============\n{prev.get_results()}')


if __name__ == '__main__':
    main()
