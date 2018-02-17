p = float(input('digite o preço? R$'))
des = float(input('digite o desconto'))
v = p - (p * des / 100)
print('Serão abatidos {:.2f}R$ e você pagara {:.2f}R$'.format(des, v))