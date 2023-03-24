from sem06_task02 import guess

low = int(input('Input low limit: '))
high = int(input('Input high limit: '))
attempts = int(input('Input attempts amount: '))

if guess(low, high, attempts):
    print('Right')
else:
    print('Wrong')
