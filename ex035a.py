print('SEJA BEM VINDO AO CALCULADOR DE PORCENTAGEM')
v = float(input('Qual o valor total :'))
p = float(input('Qual a porcentagem desse valor que deve ser calculada :'))
print('{:.0f}% de {:.2f} equivalem a {}.'.format(p, v, v*p/100))
