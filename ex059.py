from time import sleep

w = 0
a = float(input('Digite um valor: '))
b = float(input('Digite outro valor: '))
while w == 0:
    d = 1
    print('''
    [1]SOMAR
    [2]MULTIPLICAR
    [3]MAIOR
    [4]NOVOS NUMEROS
    [5]SAIR''')
    sleep(5)
    c = int(input('OPÇÃO: '))

    if c == 1:
        print('{} + {} = {}'.format(a, b, a + b))
        sleep(3)
    elif c == 2:
        print('{} * {} = {}'.format(a, b, a * b))
        sleep(3)
    elif c == 3:
        if a > b:
            print('O maior número é: {} '.format(a))
            sleep(3)
        elif a < b:
            print('O maior número é: {}'.format(b))
            sleep(3)
        else:
            print('Os números {} e {} são iguais ! '.format(a, b))
            sleep(3)
    elif c == 5:
        w = 1
        print('Saindo...')
        sleep(2)
        print('Obrigado ! Até a proxima !')
    elif c == 4:
        w = 1
        while w == 1:
            a = float(input('Digite um valor: '))
            b = float(input('Digite outro valor: '))
            w = 0
    else:
        sleep(1)
        print('Opção invalida ! Escolha novamente !')
