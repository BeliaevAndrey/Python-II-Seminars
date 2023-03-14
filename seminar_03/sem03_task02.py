# Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
# целое положительное число
# вещественное положительное или отрицательное число
# строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
# строку в верхнем регистре в остальных случаях
import re

item = input('Enter your text: ')
pattern = re.compile("-?\\d+\\.\\d+")
pattern_int = re.compile("\\d+")

if pattern.match(item):
    item = float(item)
elif pattern_int.match(item):
    item = int(item)
else:
    for i in item:
        if i.isupper():
            item = item.lower()
            break
    else:
        item = item.upper()

print(item, type(item))
