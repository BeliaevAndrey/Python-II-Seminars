# Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя
# в множестве используйте магический метод проверки на равенство пользователей. Если такого пользователя нет,
# вызывайте исключение доступа. А если пользователь есть, получите его уровень из множества пользователей.
# добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.
from s13_t04 import forming_fun, User
from s13_t03 import AccessError, LevelError
ALLOWED_LEVEL = 5


class TaskFive:

    def __init__(self, file_name: str) -> None:
        self.users_set = forming_fun(file_name)
        self.authorized = []

    def entrance(self):
        while True:
            try:
                u_id = int(input('input user ID: '))
                break
            except ValueError as exc:
                print(f'{exc.__class__.__name__} {exc}      -- Integers only!')

        u_name = input('input user Name: ')
        tmp_user = User('0', str(u_id), u_name)
        for i_user in self.users_set:
            if i_user == tmp_user:
                i_acs_level = i_user.acs_level
                break
        else:
            raise AccessError
        if i_acs_level < ALLOWED_LEVEL:
            raise LevelError
        tmp_user.acs_level = i_acs_level
        self.authorized.append(tmp_user)

    def get_authorized(self):
        return self.authorized


def main():
    task_five = TaskFive('index.json')
    task_five.entrance()
    print(task_five.get_authorized())


if __name__ == '__main__':
    main()
