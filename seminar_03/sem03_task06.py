# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# Строки нумеруются начиная с единицы
# Слова выводятся отсортированными согласно кодировки Unicode
# Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки

string = input('Input your text: ').split()

string.sort()
longest = max((len(word) for word in string))
for num, word in enumerate(string, start=1):
    print(f'{num:<} {word:>{longest}}')
