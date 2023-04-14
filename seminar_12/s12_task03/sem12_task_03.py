# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.
class Generator:
    def __init__(self, start: int, stop: int, step: int = 1):
        self.fct_range = [*range(start, stop, step)]

    @staticmethod
    def calc(limit) -> int:
        if limit < 0:
            raise ValueError("Incompatible value")
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
    factorials = Generator(5, 10, 2)
    print(factorials)
    for i in factorials:
        print(i)
    factorials = Generator(1, 5, 1)
    print(factorials)
    for i in factorials:
        print(i)


if __name__ == '__main__':
    main()
