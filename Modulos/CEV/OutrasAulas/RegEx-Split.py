import re #RegEx
#texto
texto = "Curso de Python do CFB Cursos, canal no Youtube"
#split
res = re.split(" ",texto)
#coleção com valores splitados
print(res)