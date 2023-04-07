# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

class Rectangle:

    def __init__(self, width: float, length: float = None) -> None:
        self.width = width
        self.length = length if length else width

    def get_perimeter(self) -> float:
        return 2 * (self.width + self.length)

    def get_area(self) -> float:
        return self.width * self.length


def main():
    a_rect = Rectangle(10, 20)
    print(a_rect.get_perimeter())
    print(a_rect.get_area())
    b_rect = Rectangle(100)
    print(b_rect.get_perimeter())
    print(b_rect.get_area())


if __name__ == '__main__':
    main()
