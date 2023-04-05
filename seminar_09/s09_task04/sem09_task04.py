# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой функции.

def decorator(count: int):
    def decorator2(func):
        counter = []

        def wrapper(*args, **kwargs):
            for _ in range(count):
                res = func(*args, **kwargs)
                counter.append(res)
            return counter

        return wrapper

    return decorator2


@decorator(10)
def funny_fun():
    return 100


def main():
    out = funny_fun()
    print(out, len(out))


if __name__ == '__main__':
    main()
