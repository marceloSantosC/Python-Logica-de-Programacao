a = input('Qual frase ?')
a1 = a.replace(' ', '')
b = a1[::-1]
if a1 in b:
    print('{} É um palíndromo !'.format(a))
else:
    print('{} NÃO é um palindromo !'.format(a))
