n1 = float(input('Digite o valor em metros!'))
km = n1 / 1000
hm = n1 / 100
dam = n1 / 10
m = n1
dm = n1 * 10
cm = n1 * 100
mm = n1 * 1000
print('O valor em Kilômetros é {}\nO valor em Hectômetros é {}\n'
      'O valor em Decâmetros é {}\nO valor em Metros é {}\n'
      'O valor em Decimetros é {}\nO valor em Cemtimetros é {}\n'
      'O valor em Milímetros é {}'.format(km,hm,dam,m,dm,cm,mm))