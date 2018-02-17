f = str(input('Digite uma frase: ')).strip().lower()
print('A letra A aparece {} vez na frase'.format(f.count('a')))
print('Ela aparece pela primeira vez na posição {}'.format(f.find('a')+1))
print('Ela aparece pela ultima vez na posição {}'.format(f.rfind('a')+1))

