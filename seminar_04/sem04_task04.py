# Функция получает на вход список чисел.
# Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# Как вариант напишите сортировку пузырьком. Её описание есть в википедии.
import random


def gen_list(low: int = 0, high: int = 100, step: int = 1) -> list[int]:
    num_list = [*(range(low, high + 1, step))]
    random.shuffle(num_list)
    return num_list


def bubble_sort(lst_in: list[int]):
    for i in range(len(lst_in)):
        for j in range(len(lst_in)):
            if lst_in[j] > lst_in[i]:
                lst_in[j], lst_in[i] = lst_in[i], lst_in[j]


def main():
    num_list = gen_list(20, 101, 3)
    print(num_list)
    bubble_sort(num_list)
    print(num_list)


if __name__ == '__main__':
    main()
