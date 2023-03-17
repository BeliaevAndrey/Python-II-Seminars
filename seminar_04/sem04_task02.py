STRING = '''Напишите функцию, которая принимает строку текста. 
Сформируйте список с уникальными кодами Unicode каждого 
символа введённой строки отсортированный по убыванию.
'''


def order(str_in: str) -> list:

    return sorted(map(ord, set(str_in)), reverse=True)


def main():
    print(order(STRING))


if __name__ == '__main__':
    main()
