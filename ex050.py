soma = 0
cont = 0
for r in range(1, 7):
    num = int(input('Digite o {}º valor:'.format(r)))
    if num % 2 == 0:
            soma += num
            cont += 1
print('A soma dos {} números pares é igual a: {}'.format(cont, soma))