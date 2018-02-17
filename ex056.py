IDADE = 0
maior = 0
sub20 = 0
velho = 0
for r in range(1, 5):
    print('Informe os dados da pessoa {}'.format(r))
    nome = str(input('Nome: '))
    sexo = str(input('Sexo M/F: '))
    idade = int(input('Idade: '))
    print('-' * 25)
    IDADE += idade
    if r == 1 and sexo in 'Mm':
        maior = idade
        velho = nome
    if idade > maior and sexo in 'Mm':
        maior = idade
        velho = nome
    elif sexo in 'Ff' and idade < 20:
        sub20 += 1
print('O homem mais velho é {} de {} anos'.format(velho.capitalize(), maior))
print('{} mulheres tem menos de 20 anos.'.format(sub20))
print('A média de idade do grupo é de {.:2f} anos'.format(IDADE / 4))
