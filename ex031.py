d = float(input('Qual a distancia da viagem? (em km)'))
if d <= 200:
    print('O preço final da viagem é de : R${:.2f}'.format(d*0.50))
else:
    print('O preço final da viagem é de : R${:.2f}'.format(d*0.45))
