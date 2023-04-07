# Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения возраста на год, full_name
# для вывода полного ФИО и т.п. на ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого изменения,
# но есть возможность получить текущий возраст

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


def main():
    first = Human('John', 'Doe', 'Dawson', 54)
    first.birthday()
    print(first.get_full_name())
    print(f'age 1: {first.get_age()}')
    print(f'{first._Human__age=}')
    first.__age += 100
    print(f'age 2: {first.get_age()}')


if __name__ == '__main__':
    main()
