# Создайте класс с базовым исключением и дочерние классы-исключения:
# - ошибка уровня,
# - ошибка доступа.

class OwnBasicException(Exception):
    def __init__(self,  message: str):
        self.message = message

    def __str__(self):
        return f'{self.message}'


class LevelError(OwnBasicException):
    def __init__(self):
        super(LevelError, self).__init__('Wrong Level')


class AccessError(OwnBasicException):
    def __init__(self):
        super(AccessError, self).__init__('Access Denied')


def main():
    # raise LevelError
    raise AccessError


if __name__ == '__main__':
    main()
