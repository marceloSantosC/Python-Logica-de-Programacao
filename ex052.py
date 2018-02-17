a = int(input('Digite um número: '))
ct = 0
for r in range(1, a + 1):
    if a % r == 0:
        ct += 1
if ct != 2:
    print('{} NÃO é um número primo pois foi divisivel {} vezes !'.format(a, ct))
else:
    print('{} É um número primo pois foi divisivel apenas {} vezes !'.format(a, ct))
