p = float(input('Qual o seu peso ?'))
a = float(input('Qual a sua altura ?'))
imc = p / (a ** 2)
if imc < 18.5:
    print('Seu imc é de {:.2f}, você esta abaixo do peso !'.format(imc))
elif  18.5 <= imc < 25:
    print('Seu imc é de {:.2f}, você esta no peso ideal !'.format(imc))
elif 25 <= imc < 30:
    print('Seu imc é de {:.2f}, você esta acima do peso !'.format(imc))
elif 30 <= imc < 40:
    print('Seu imc é de {:.2f} , você esta obeso !'.format(imc))
elif imc >= 40:
    print('Seu imc é de {:.2f}, você esta com obsesidade morbida !'.format(imc))

