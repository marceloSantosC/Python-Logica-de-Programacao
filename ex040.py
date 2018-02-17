n1 = float(input('Qual foi sua nota no 1º semestre ?'))
n2 = float(input('Qual foi sua nota no 2º semestre ?'))
m = (n1+n2)/2
if m < 5:
    print('Você foi reprovado com {:.2f} pontos abaixo da média. Sua media foi de {:.2f}'.format(5 - m), m)
elif 7 > m >= 5:
    print('Sua média foi de {:.2f} você esta em recuperação !'.format(m))
elif m >= 7:
    print('Você foi aprovado com {:.2f} pontos acima da media, sua media foi de {:.2f}'.format(m - 6.9, m))

