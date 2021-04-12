import sqlite3
from sqlite3 import Error

def conexao():
    caminho = 'C:\\temp\\PY-VSCODE-2020\\SQLite\\Agenda.db'
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    else:
        return con

def consulta(conexao,sql):
    c=conexao.cursor()
    c.execute(sql)
    res = c.fetchall()
    return res

vsql='SELECT * FROM tb_contatos '
vcon = conexao()
resgistro = consulta(vcon,vsql)

for r in resgistro:
    print(r)

#WHERE COLUNA LIKE "%A%"