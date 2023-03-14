
string ="""Пользователь вводит строку текста.
Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
Результат сохраните в словаре, где ключ - символ, а значение - частота встречи символа в строке.
Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.
"""

first_count = {smb: string.count(smb) for smb in string}

second_without_count = {}

for smb in string:
    if smb in second_without_count.keys():
        second_without_count[smb] += 1
    else:
        second_without_count[smb] = 1

print(first_count, '\n')
print(second_without_count)

print(second_without_count == first_count)
