a = float(input('Segmento um :'))
b = float(input('Segmento dois :'))
c = float(input('Segmento três :'))
zug = 0
if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        zug = ('Equilátero')
    elif a != c != b != a:
        zug = ('Escaleno')
    else:
        zug(' isosceles ')
    print('É possivel formar um triangulo {} com esses segmentos'.format(zug.lower()))
else:
    print('Não é possivel formar um triangulo com esses segmentos !')