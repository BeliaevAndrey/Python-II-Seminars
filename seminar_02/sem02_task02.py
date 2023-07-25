import sys

data = [
    1,
    1.2,
    "str",
    [],
    {},
    set(),
    (1,),
    False,
    type('Own', (object, ), {'__str__': 'lambda: "own"'})
]

for i, var in enumerate(data, start=1):
    print(f'{i:0>4}: var={str(var):<25} id(var)={id(var):<20} sys.getsizeof(var)={sys.getsizeof(var):<10}', end=' ')
    try:
        print(f'hash(var)={hash(var):<30}', end=' ')
    except TypeError:
        print(f'{"Unhashable":<40}', end=' ')
    print(f'str(type(var))={str(type(var)):<25}', end=' ')
    print()
