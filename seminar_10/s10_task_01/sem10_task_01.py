# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.
from math import pi as PI


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def get_length(self) -> float:
        return 2 * PI * self.radius

    def get_area(self) -> float:
        return PI * self.radius ** 2


def main():
    a_circle = Circle(2)
    print(a_circle.get_length())
    print(a_circle.get_area())


if __name__ == '__main__':
    main()
