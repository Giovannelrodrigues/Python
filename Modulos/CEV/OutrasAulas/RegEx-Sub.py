import re #RegEx
#texto
texto = "Curso de Python do CFB Cursos, canal no Youtube"
#substituir
res = re.sub(' ','|',texto)
#retorna string substituida
print(res)