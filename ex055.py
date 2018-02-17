maior = 0
menor = 0

for r in range(1, 6):
    a = float(input('Peso da {}ª pessoa: '.format(r)))
    if r == 1:
        maior = a
        menor = a
    else:
        if r > maior:
            maior = a
        elif r < menor:
            menor = a
print('O menor peso foi {}KG e o maior foi {}KG'.format(menor, maior))
