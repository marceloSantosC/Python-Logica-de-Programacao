from random import randint

print('-' * 50)
print('Vou pensar em um número de 0 a 10, tente descobrir qual !')
a = randint(0, 10)
ct = 0
t = 9
j = int(input('Em que número pensei ?'))
while j != a:
    ct += 1
    t += -1
    print('Você errou ! Tente de novo !')
    j = int(input('Em que número pensei ?'))
    print('Voce tem {} tentativas !'.format(t))
    if t == 0:
        j = a
        print('Você perdeu ! suas tentativas acabaram. O número era {}'.format(a))
if ct == 0:
    print('UAU ! Você é incrivel, acertou de primeira !')
if ct > 0 and t != 0:
    print('Você descobriu o nùmero na {}ª tentativa ! Parabéns ! '.format(ct))
