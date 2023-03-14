# Три друга взяли вещи в поход. Сформируйте словарь, где ключ - имя друга, а значение - кортеж вещей. Ответьте на вопросы:
# какие вещи взяли все три друга
# какие вещи уникальны, есть только у одного друга
# какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

FRIENDS = {
    'first': ('fishing rod', 'ball', 'book', 'backpack', 'hooks', 'knife', 'boat', 'own unique FIRST THING'),
    'second': ('fishing rod', 'tent', 'sleeping bag', 'backpack', 'hooks', 'knife', 'own unique SECOND THING'),
    'third': ('matches', 'salt', 'pot', 'book', 'lantern', 'backpack', 'knife', 'own unique THIRD THING'),
}

all_things = set([item for items in FRIENDS.values() for item in items])
# for item in FRIENDS.values():
#     all_things.update(set(item))

print(f'Totally things for all persons:\n{"-"*31}')
print('; '.join(all_things))

common_things = set(all_things)
print(f'\ncommons:\n{common_things}\n\n')

print(f'\nUnique things for everyone:\n{"-"*27}')
for friend in FRIENDS:
    print(f'{friend+":":15}', end='')
    others = tuple(pers for pers in FRIENDS.keys() if pers != friend)
    things = set(item for item in (items for key in others for items in FRIENDS[key]))
    unique = set(FRIENDS[friend]).difference(things)
    common_things.difference_update(unique)
    print('; '.join([*sorted(unique, key=len, reverse=True)]))

print(f'\ncommons:\n{common_things}\n\n')
print(f'\nLack of things for everyone:\n{"-"*27}')      # TODO: Needs to be finished. But later
for friend in FRIENDS:
    print(f'{friend+":":15}', end='')
    absent_things = set(FRIENDS[friend]).difference(common_things)
    print('; '.join([*(sorted(absent_things, key=len, reverse=True))]))


