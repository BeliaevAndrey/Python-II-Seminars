# Вспомните какие модули вы уже проходили на курсе.
# Создайте файл, в котором вы импортируете встроенные в
# модуль функции под псевдонимами. (3-7 строк импорта).


from random import randint as r_int
from random import random as r_rnd
from time import time as t_tm_s
from time import time_ns as t_ns
from collections import OrderedDict as _OrDct
from array import array as _arr
from collections import deque as _dq

print('r_int(1, 100)', r_int(1, 100))
print('r_rnd(1, 100)', r_rnd())
print('t_tm_s', t_tm_s())
print('t_ns', t_ns())
print('_OrDct.fromkeys(*range(1, 10))', _OrDct.fromkeys(range(1, 10)))
print('arr', _arr('d', (1, 2, 3, 4)))
a = _dq()
a.append(10)
print(a)
