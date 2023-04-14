# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.
class Generator:

    def __init__(self, *args):
        start, stop, step = 1, 1, 1
        match len(args):
            case 3:
                start, stop, step = args
            case 2:
                start, stop = args
            case 1:
                stop = args[0]
            case 0:
                raise AttributeError("At least 'stop' value needed")
            case _:
                raise AttributeError("Function takes up to 3 parameters: 'start', 'stop', 'step'")
        if start == stop:
            self.fct_range = [stop]
        elif start > stop:
            raise AttributeError("'start' parameter must be greater than or equal to 'stop' parameter")
        else:
            self.fct_range = [*range(start, stop, step)]

    @staticmethod
    def calc(limit) -> int:
        if limit < 0:
            raise ValueError(f'Incompatible value (lesser than 0): {limit}')
        if limit in (0, 1):
            return 1
        result = 1
        for i in range(1, limit + 1):
            result *= i
        return result

    def __iter__(self):
        return self

    def __next__(self):
        if self.fct_range:
            return self.calc(self.fct_range.pop(0))
        raise StopIteration

    def __str__(self):
        return f'Factorials range: {self.fct_range}'


def main():
    factorials = Generator(0, 81, 20)
    print(factorials)
    for i in factorials:
        print(i)
    factorials = Generator(10, 10)
    print(factorials)
    for i in factorials:
        print(i)


if __name__ == '__main__':
    main()
