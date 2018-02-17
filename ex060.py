'''from math import factorial

n = int(input('Digite um número para calcular seu fatorial: '))
print('{}! = {}'.format(n, factorial(n)))

n = int(input('Digite o número que sera fatorado: '))
c = n
f = 1
print('{}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
print('-')
print('USANDO O COMANDO FOR')'''

n = int(input('Digite o número que sera fatorado: '))
fat = 1
print('{}! = '.format(n), end='')
for r in range(n, 0, -1):
    print(r, end='')
    print(' = ' if r == 1 else ' x ', end='')
    fat *= r
print(fat)

