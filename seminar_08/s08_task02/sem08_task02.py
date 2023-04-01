# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.
import json
import os


def write(user_name: str, user_id: str, level_id: str, file_name: str = 'index.json') -> None:
    if not os.path.isfile(file_name):
        with open(file_name, 'w', encoding='utf-8') as f_out:
            users_dct = {level_id: {user_id: user_name}}
            json.dump(users_dct, f_out, indent=4)
    else:
        with open(file_name, 'r', encoding='utf-7') as f_in:
            users_dct: dict = json.load(f_in)
        if level_id in users_dct:
            users_dct.get(level_id)[user_id] = user_name
        else:
            users_dct[level_id] = {user_id: user_name}
        with open(file_name, 'w', encoding='utf-8') as f_out:
            json.dump(users_dct, f_out, indent=4)


def ask_user(file_name: str) -> None:
    with open(file_name, 'r', encoding='utf-8') as f_in:
        users_dict = json.load(f_in)
    users_ids = [i_key for vals in users_dict.values() for i_key in vals]
    while True:
        name = input('Enter name (EXIT to stop): ')
        if name == 'EXIT':
            break
        while True:
            user_id = input('Enter UID: ')
            if user_id not in users_ids:
                break
        level_id = input('Enter level ID: ')
        while int(level_id) not in range(1, 8):
            level_id = input('Enter level ID: ')
        write(name, user_id, level_id)


def main():
    print(os.getcwd())
    ask_user('index.json')


if __name__ == '__main__':
    main()