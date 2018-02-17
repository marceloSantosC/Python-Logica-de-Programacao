from datetime import date
a = date.today().year
print(a)
np = 0
nb = 0
for r in range(1, 8):
    nb += 1
    b = int(input('Ano de nascimento da {}ª pessoa : '.format(nb)))
    if a - b >= 18:
        np += 1
print('{} dessas pessoa(s) são maiores de 18 anos !'.format(np))
print('{} dessas pessoa(s) são menores de idade !'.format(7 - np))
