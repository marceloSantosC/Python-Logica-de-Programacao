''' import math
a = int(input('por favor digite um angulo'))
# s = math.hypot(a)
c = math.cos(a)
t = math.tan(a)
print(c, t) '''
from math import hypot
co = float(input('Comprimento do cateto oposto'))
ca = float(input('Comprimento do cateto adjacente'))
hi = (co ** 2 + ca ** 2) ** (1/2)
# ou
# hi= hypot(co, ca)
print('A hipotunesa mede {:.2f}'.format(hi))


