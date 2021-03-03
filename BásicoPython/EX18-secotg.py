import math
an = float(input('Digite o valor do ângulo'))
se = math.sin(math.radians(an))
print('O valor do seno de {}° é {:.2f}'.format(an,se))
co = math.cos(math.radians(an))
print('O valor do cosseno de {}° é {:.2f}'.format(an,co))
tg = math.tan(math.radians(an))
print('O valor da tangente de {} é {:.2f}'.format(an,tg))