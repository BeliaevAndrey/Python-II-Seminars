# Самостоятельно сохраните в переменной строку текста.
# Создайте из строки словарь, где ключ - буква, а значение - код буквы.
# Напишите преобразование в одну строку.
def main():
    variable = "Самостоятельно сохраните в переменной строку текста."
    final = {ch: ord(ch) for ch in variable}
    print(final)


if __name__ == '__main__':
    main()
    