"""
Нарисовать в консоли ёлку спросив у пользователя количество рядов.
Пример результата:
Сколько рядов у ёлки? 5
    *
   ***
  *****
 *******
*********
"""

rows = 50  # int(input("Number of rows: "))
width = rows * 2 + 1
for i in range(rows):
    string = ' ' * ((width - (2 * i + 1)) // 2) + '*' * (2 * i + 1)
    print(string)

for i in range(rows):
    print(f'{"*" * (2 * i + 1):^{width}}')
