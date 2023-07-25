# Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
# Используйте комплексные числа для извлечения квадратного корня.
# d = b ** 2 - 4 * a * c
# x1 = (-b + sqrd) / (2 * a)
# x2 = (-b - sqrd) / (2 * a)

def calc_d(a, b, c) -> float:
    return b ** 2 - 4 * a * c


def calc_roots(a, b, c, d: [float, complex]):
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    return x1, x2


def main():
    a: float = float(input('input a: '))
    b: float = float(input('input b: '))
    c: float = float(input('input c: '))
    d: float = calc_d(a, b, c)
    if d > 0:
        x1, x2 = calc_roots(a, b, c, d)
        print(f'roots are: {x1=}; {x2=}')
    elif d == 0:
        print(f'{(-b) / (2 * a)}')
    else:
        d: complex = complex(d, 0)
        x1, x2 = calc_roots(a, b, c, d)
        print(f'roots are: {x1=:.2}; {x2=:.2}')


if __name__ == '__main__':
    main()
