# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)
from time import time


class MyString(str):
    """Extends str"""

    def __new__(cls, content: str, author: str) -> 'MyString':
        instance = super().__new__(cls, content)
        instance.content = content
        instance.author = author
        instance.created = time()
        return instance

    # def __str__(self) -> str:
    #     return self.instance.content


def main():
    new_string = MyString('test string', 'Me myself')
    print(new_string.upper())
    print(new_string.isdigit())
    print(new_string.isalpha())
    print(new_string.isprintable())
    print(new_string.author)
    print(new_string.created)


if __name__ == '__main__':
    main()
