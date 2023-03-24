from sem06_task03 import guess, argv
# from sys import argv

if not argv:
    low = 10
    high = 100
    attempts = 10
else:
    low, high, attempts = map(int, argv[1:])
    print('limits:', low, high, attempts)


if guess(low, high, attempts):
    print('Right')
else:
    print('Wrong')
