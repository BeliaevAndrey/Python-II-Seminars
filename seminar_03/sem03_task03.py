# Создайте вручную кортеж содержащий элементы разных типов.
#   Получите из него словарь списков, где
#       ключ - тип элемента,
#       значение - список элементов данного типа.

tuple_under_treat = (True, False,
                     1, 2, 3,
                     'a', 'b', 'c', 'd',
                     1.1, 1.2, 1.3,
                     ['a', 'b'],
                     (1,), (2, 3),
                     {1: 2, 2: 3, },
                     {1, 2, 3, 4, },
                     )

final_dict = {}
for item in tuple_under_treat:
    key = str(type(item))[8:-2]
    if key not in final_dict.keys():
        final_dict[key] = [item]
    else:
        final_dict[key].append(item)

for item in final_dict.items():
    print(item)
