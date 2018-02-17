s = float(input('Qual o salario em R$'))
if s > 1250.00:
    a = 10
else:
    a = 15
print('Você recebe {:.2f} e com o aumento  salarial de {}% recebera mais R${:.2f} somando um total de R${:.2f}.'.format(s, a, s*a/100, s*a/100+s))
