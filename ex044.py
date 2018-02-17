p = float(input('Qual o preço do produto ?'))
print('''Por favor escolha uma das condiçoes de pagamento
1. Á vista em dinheiro ou cheque. Recebendo 10% de desconto.
2. Á vista no cartão. Recebendo 5% de desconto.
3. Em até 2x no cartão pagando o preço normal.
4. Em 3x ou mais no cartão pagando 20% de juros.''')
o = int(input('Qual sua escolha de pagamento ?'))
if o == 1:
    pf = p - (p*10/100)
    print('Você escolheu a opção 1 Você pagara R${:.2f} á vista.'.format(pf))
elif o == 2:
    pf = p - (p*5/100)
    print('Você escolheu a opção 2 e pagara R${:.2f}'.format(pf))
elif o == 3:
    pf = p/2
    print('Você escolheu a opção 3 e pagara 2 parcelas de R${} somando um total de R${}'.format(pf, p))
elif o == 4:
    pc = int(input('O produto sera parcelado em quantas vezes ?'))
    pf = ((p*20/100)+p)
    pf2 = pf/pc
    print('Você escolheu a opçao 4 e pagara {} parcelas de R${:.2f} somando um total de R${} com juros inclusos'.format(pc, pf2, pf))
else:
    print('Por favor selecione uma opção de compra valida !')
