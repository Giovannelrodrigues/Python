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

def delete(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    else:
        print('Deletado com sucesso')


vsql = f'DELETE FROM tb_contatos WHERE N_IDCONTATO=5'
vcon = conexao()
delete(vcon, vsql)