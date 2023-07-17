# Создайте несколько переменных разных типов. Проверьте к какому типу относятся созданные переменные.

a = 1
b = 5.2
c = "str"
d = []
e = set()
f = {}
g = 1,
h = True
i = 1,

for var in a, b, c, d, e, f, g, h, i:
    print(var, type(var))
    print(var.__class__.__name__)
