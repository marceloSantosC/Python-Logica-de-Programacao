n = str(input('Digite seu nome')).strip().title()
print('Prazer em te conhecer {}'.format(n.title()))
n1 = n.split()
print('Seu primeiro nome é: {}'.format(n1[0]))
print('Seu ultimo nome é: {}'.format(n1[-1]))
#  ...
print('{}'.format('-'* 900))