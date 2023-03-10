import sys

data = [
    1,
    1.2,
    "str",
    [],
    {},
    set(),
    (1,)
]

for i, var in enumerate(data, start=1):
    print(f'{i}: {var=} ,{id(var)=}, {sys.getsizeof(var)=}', end=' ')
    try:
        print(f'{hash(var)=}', end=' ')
    except TypeError:
        print(f'Unhashable', end=' ')
    if isinstance(var, int):
        print(f'{type(var)=}', end=' ')
    elif isinstance(var, str):
        print(f'{type(var)=}', end=' ')
    print()
