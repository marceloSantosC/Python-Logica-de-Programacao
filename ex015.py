km = float(input('quantos KM foram rodados?'))
d = int(input('quantos dias ficou alugado?'))
p = (km * 0.15) + (d * 60)
print('o total a pagar fi cou em R${:.2f}2'.format(p))