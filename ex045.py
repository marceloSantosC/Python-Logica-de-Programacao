from random import randint
item = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0,2)
print('{}'.format(item[pc]))
print('''Digite o numero que corresponde a sua escolha
0 - PEDRA
1 - PAPEL
2 - TESOURA''')
player = int(input('Escolha: '))
if player == 0 or player == 1 or player == 2:
    print('''    JO
    KEN
    PO''')
    print('Eu joguei {} e você jogou {}.'.format(item[pc], item[player]))

    if player == pc:
        print('EMPATE !')
    elif player == 0 and pc == 2:
        print('VOCÊ VENCEU!')
    elif player == 1 and pc == 0:
        print('VOCÊ VENCEU!')
    elif player == 2 and pc == 1:
        print('VOCÊ VENCEU!')
    elif player == 2 and pc == 0:
        print('EU VENCI!')
    elif player == 0 and pc == 1:
        print('EU VENCI!')
    elif player == 1 and pc == 2:
        print('EU VENCI!')
    elif 0 < player > 2:
        print('POR FAVOR SELECIONE O NUMERO CORRESPONDENTE A SUA JOGADA!')
else:
    print('JOGADA INVALIDA!')