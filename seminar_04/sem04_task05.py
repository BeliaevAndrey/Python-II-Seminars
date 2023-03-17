# Функция принимает на вход три списка одинаковой длины:
# имена str,
# ставка int,
# премия str с указанием процентов вида “10.25%”.
# Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии
from decimal import Decimal


def joiner(name_lst: list[str],
           salary_lst: list[int],
           award_lst: list[str],
           ) -> dict[str, float]:
    award_lst = list(map(
        lambda x:
        Decimal(x.replace('%', '')) / 100, award_lst
    ))

    return {name: float(salary * award) for
            name, salary, award in
            zip(name_lst, salary_lst, award_lst,)}


def main() -> None:
    name_lst: list[str] = ['First', 'Second', 'Third']
    salary_lst: list[int] = [120, 100, 140]
    award_lst: list[str] = ['10.25%', '7.75%', '8.95%']
    print(joiner(name_lst,
                 salary_lst,
                 award_lst,
                 ))


if __name__ == '__main__':
    main()
