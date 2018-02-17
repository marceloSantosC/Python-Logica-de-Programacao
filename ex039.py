from datetime import date
s = str(input('Sexo (Masculino ou Feminino): ')).lower()
f = ['feminino', 'masculino']
if s == f[0]:
    print('Pessoas do sexo feminino não são obrigadas a se alistar!')
elif s == f[1]:
    a = int(input('Em que ano você nasceu ?'))
    A = date.today().year
    i = A - a
    if i < 18:
        print('Ainda não é tempo de se alistar.Você se alistara em {} ano(s).'.format(18-i))
    elif i == 18:
        print('É hora de se alistar.Procure informaçoes em sites oficiais.')
    else:
        print('Se você ainda não se alistou você esta atrasado em {} ano(s).'.format(i-18))
else:
    print('Por favor digite um sexo valido !')
print('-'*70)
