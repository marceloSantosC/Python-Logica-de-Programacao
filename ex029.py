v = float(input('Qual a velocidade ?'))
if v > 80.0:
    m = (v-80) * 7
    print('Você foi multado em R${:.2f} por excesso de velocidade. Respeite as leis de transito e dirija com segurança !'.format((v-80)*7))
else:
    print('Continue a dirigir com segurança, tenha um bom dia !')