from random import randint
from time import sleep
print('Estou pensando em um numero de 0 a 5, tente adivinhar qual!')
sleep(3)
e = randint(0, 5)
p = int(input('Qual foi o número em que pensei ?'))
if p == e:
    print('Você advinhou o número realmente era {}. Você é incrivel !'.format(e))
else:
    print('Eu ganhei o número era {} e não {}!'.format(e, p))