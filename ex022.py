'''n = str(input('Informe o nome completo por favor')).strip()# use para evitar problemas com espaços antes da escrita
print('Seu nome em maiuscula é: {}'.format(n.upper()))
print('Seu nome em minusculas é: {}'.format(n.lower()))
na = n.replace(' ', '')
print('Seu nome contém {} letras'.format(len(na)))
print('Seu primeiro nome contém {} letras'.format(len(n.split())))'''

nome = str(input('Qual seu nome completo'))
print('Em maiusculas {}'.format(nome.upper()))
print('Em minusculas {}'.format(nome.lower()))
print('Ele tem {} letras'.format(len(nome) - nome.count(' ')))
# print('O primeiro nome tem {} letras'.format(nome.find(' ')))
s = nome.split()
print('seu primeiro nome é {} e tem {} letras'.format(s[0], len(s[0])))


