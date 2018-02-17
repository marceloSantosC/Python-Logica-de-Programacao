from datetime import date
n = int(input('Qual o ano de nascimento do atleta ?'))
a = date.today().year
i = a-n
print('Idade:', i)
if i <= 9:
    print('Categoria: Mirim')
elif i <= 14:
    print('Categoria: Infantil')
elif i <= 19:
    print('Categoria: Júnior')
elif i <= 25:
    print('Categoria: Sénior')
else:
    print('Categoria: Master')
