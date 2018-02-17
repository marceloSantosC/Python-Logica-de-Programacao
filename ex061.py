a = int(input('Primeiro termo: '))
b = int(input('Razão: '))
c = 0
d = 0
while c < 10:
    c += 1
    if b == +b:
        print('{}'.format(a + d), end='')
    elif b == -b:
        print('{}'.format(a - d), end='')
    print(', ' if c < 10 else '', end='')
    d += b
