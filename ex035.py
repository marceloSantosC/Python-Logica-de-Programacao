a = float(input('Segmento um :'))
b = float(input('Segmento dois :'))
c = float(input('Segnmento três :'))
if a < b + c and b < a + c and c < a + b:
    print('É possivel formar um triangulo com esses segmentos!')
else:
    print('Não é possivel formar um triangulo com esses segmentos!')