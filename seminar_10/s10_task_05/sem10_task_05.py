# Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

class Mammal:

    def __init__(self, name: str, age: int, hair: str, voice: str):
        self.name = name
        self.age = age
        self.hair = hair
        self.voice = voice

    def get_info(self) -> str:
        return (f'name:  {self.name}'
                f'\nage:   {self.age}'
                f'\nhair:  {self.hair}'
                f'\nvoice: {self.voice}'
                )


class Bird:

    def __init__(self, name: str, age: int, color: str, voice: str):
        self.name = name
        self.age = age
        self.color = color
        self.voice = voice

    def get_info(self) -> str:
        return (f'name:  {self.name}'
                f'\nage:   {self.age}'
                f'\ncolor: {self.color}'
                f'\nvoice: {self.voice}'
                )


class Fish:

    def __init__(self, name: str, age: int, color: str):
        self.name = name
        self.age = age
        self.color = color

    def get_info(self) -> str:
        return (f'name:   {self.name}'
                f'\nage:   {self.age}'
                f'\ncolor: {self.color}'
                )


def main():
    a_bird = Bird('Raven', 10, 'black', 'crow')
    a_dog = Mammal('Snoopy', 5, 'pale', 'woof')
    a_fish = Fish('Fishy', 1, 'rainbow')
    print(a_bird.get_info())
    print()
    print(a_dog.get_info())
    print()
    print(a_fish.get_info())
    print()

    
if __name__ == '__main__':
    main()