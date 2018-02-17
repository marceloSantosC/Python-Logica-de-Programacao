ti = int(input('Primeiro termo: '))
ra = int(input('Razão: '))
for r in range(1, 11):
    ti += ra
    print(ti, end=' ')
print('. Acabou')