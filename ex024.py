c = str(input('Em que cidade você nasceu ?')).strip()
s = c.lower()
print('santo' in s)
# soluçao 2

print('Parte 2')
cid = str(input('Em que cidade você nasceu?')).strip()
print(cid[:5].upper() == 'SANTO')