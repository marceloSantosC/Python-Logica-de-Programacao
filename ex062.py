a = int(input('Primeiro termo: '))
b = int(input('Razão: '))
c = 0
d = 0
e = 0
f = 10
while f != 0:
    e += f
    while c <= f:
        c += 1
        if b == +b:
            print('{}'.format(a + d), end='')
        elif b == -b:
            print('{}'.format(a - d), end='')
        print(', ' if c <= 10 else '', end='')
        d += b
        f = int(input('Quantos termos você quer mostrar a mais ?'))

