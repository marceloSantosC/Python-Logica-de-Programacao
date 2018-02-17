import random

a = str(input('nome do aluno 1'))
b = str(input('nome do aluno 2'))
c = str(input('nome do aluno 3'))
d = str(input('nome do aluno 4'))
r = [a, b, c, d]
e = random.choice(r)
print('foi sorteado o aluno {}'.format(e))
u=