# Доработаем прямоугольник и добавим экономию памяти для
# хранения свойств экземпляра без словаря __dict__.

class Rectangle:
    __slots__ = ('_width', '_length')

    def __init__(self, width: float, length: float = None) -> None:
        self._width = width
        self._length = length if length else width

    @property
    def width(self):
        return self._width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, new_len):
        if new_len <= 0:
            raise ValueError('Length cannot be lesser than or equal to 0')
        self._length = new_len

    @width.setter
    def width(self, new_width):
        if new_width <= 0:
            raise ValueError('Length cannot be lesser than or equal to 0')
        self._width = new_width

    def get_perimeter(self) -> float:
        return 2 * (self.width + self.length)

    def get_area(self) -> float:
        return self.width * self.length

    def __str__(self):
        return (f'\nRectangle: {self.width} X {self.length}'
                f'\nPerimeter: {self.get_perimeter()}'
                f'\nArea:      {self.get_area()}')

    def __repr__(self):
        return f'Rectangle({self.width}, {self.length})'


def main():
    some_rect = Rectangle(10, 20)
    print(f'{some_rect=}')
    some_rect.length = 100
    some_rect.width = 200
    print(f'{some_rect=}')
    try:
        some_rect.length = 0
    except Exception as exc:
        print(f'\033[31m{exc.__class__.__name__}:{exc}\033[0m')
    try:
        some_rect.width = -100
    except Exception as exc:
        print(f'\033[31m{exc.__class__.__name__}:{exc}\033[0m')
    print(f'{some_rect=}')
    print(some_rect.__slots__)
    print(some_rect.__dir__())


if __name__ == '__main__':
    main()
