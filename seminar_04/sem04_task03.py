# Функция получает на вход строку из двух чисел через пробел.
# Сформируйте словарь, где ключом будет символ из Unicode, а значением - целое число.
# Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до
# наибольшего включительно

def order(str_in: str) -> dict[str, int]:
    a, b = sorted(map(int, str_in.split()))
    num_lst = {chr(i): i for i in list(range(a, b + 1))}
    return num_lst


def main():
    print(order(input("Input range: ")))


if __name__ == '__main__':
    main()
