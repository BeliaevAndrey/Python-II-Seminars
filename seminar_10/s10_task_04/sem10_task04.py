# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# шестизначный идентификационный номер
# уровень доступа вычисляемый как остаток от деления суммы цифр id на семь

class Human:

    def __init__(self, f_name: str, l_name: str, patronymic: str,  age: int) -> None:
        self.f_name = f_name
        self.l_name = l_name
        self.patronymic = patronymic
        self.__age = age

    def birthday(self) -> None:
        self.__age += 1

    def get_full_name(self) -> str:
        return f'{self.l_name} {self.f_name} {self.patronymic}'

    def get_age(self) -> int:
        return self.__age


class Employee(Human):
    __DIVIDOR = 7

    def __init__(self, f_name: str, l_name: str, patronymic: str, age: int, e_id: int) -> None:
        super().__init__(f_name, l_name, patronymic, age)
        if len(str(e_id)) != 6:
            raise ValueError("Too short id!")
        self.__e_id = e_id
        self.__acs_level = self._access_level()

    def _access_level(self) -> int:
        return sum([int(smb) for smb in str(self.__e_id)]) % self.__DIVIDOR

    def get_e_id(self) -> int:
        return self.__e_id

    def get_access_level(self) -> int:
        return self.__acs_level


def main():
    first = Employee('John', 'Doe', 'Dawson', 54, 673588)
    print(f'Name: {first.get_full_name()}')
    print(f'age:  {first.get_age()}')
    print(f'E-ID: {first.get_e_id()}')
    print(f'ACL:  {first.get_access_level()}')

    second = Employee('John', 'Doe', 'Dawson', 54, 673758)
    second.birthday()
    print(f'Name: {second.get_full_name()}')
    print(f'age:  {second.get_age()}')
    print(f'E-ID: {second.get_e_id()}')
    print(f'ACL:  {second.get_access_level()}')


if __name__ == '__main__':
    main()
