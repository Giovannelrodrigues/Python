import sqlite3
from sqlite3 import Error

def ConexaoBanco():
    caminho = 'C:\\temp\\PY-VSCODE-2020\\SQLite\\Agenda.db'
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    else:
        return(con)

def atualizar(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    else:
        print('Valor atualizado')


vsql = f'UPDATE tb_contatos SET T_NOMECONTATO="Bruno", T_TELEFONECONTATO="(31)996300338",T_EMAILCONTATO="Bruno@gmail.com" WHERE N_IDCONTATO=6 '
vcon = ConexaoBanco()
atualizar(vcon,vsql)