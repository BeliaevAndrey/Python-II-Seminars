# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.
import json
from time import time


class Factorial:
    FILE_NAME = 'out_file.json'

    def __init__(self, amount: int = 1) -> None:
        self.results = []
        self.amount = amount

    def __call__(self, limit) -> list[int]:
        if limit < 0:
            raise ValueError("Incompatible value")
        if limit in (0, 1):
            self.results.append(1)
        result = 1
        for i in range(1, limit + 1):
            result *= i
            self.results.append(result)
            if len(self.results) > self.amount:
                self.results.pop(0)

        return self.results

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.FILE_NAME, 'w', encoding='utf-8') as f_out:
            json.dump(str(self.results), f_out)


#
# class FctConMan:
#
#     def __init__(self, file_name):
#         self.result_dict = {}
#         self.file_name = file_name
#
#     def __enter__(self, result):
#         self.result_dict[str(time())] = result
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         with open(self.file_name, 'w', encoding='utf-8') as f_out:
#             json.dump(self.result_dict, f_out)


def main():
    with Factorial(3) as fct:
        fct(5)


if __name__ == '__main__':
    main()
